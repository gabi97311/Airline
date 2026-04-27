from decimal import Decimal

from fastapi.responses import JSONResponse
from fastapi import Depends, HTTPException, status, Request
from typing import Optional, Any
import stripe
from faststream.rabbit import RabbitBroker

from src.models import PaymentModel
from src.payment_enum import PaymentStatus
from src.repositories import PaymentRepository
from src.schemes import PaymentCreate
from src.api_client import ApiClient
from src.config import settings
from src.exception import NotFoundException
from src.rabbit_mq.rabbitmq_client import AirlineMQClient

class PaymentService:
    def __init__(self, repo: PaymentRepository):
        self.repo = repo
        stripe.api_key = settings.STRIPE_SECRET_KEY

    async def get_payment_by_id(self, payment_id: int) -> PaymentModel:
        if not (payment := await self.repo.get_payment_by_id(payment_id)):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Payment not found"
            )
        return payment

    async def create_checkout_session(
        self, ticket_details: PaymentCreate, ticket_client: ApiClient, user_id: int
    ):

        payment = await self._verify_and_map_payment_data(
            ticket_details, ticket_client, user_id
        )

        if payment.status == PaymentStatus.succeeded:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Ticket was purchased"
            )

        if payment.stripe_url:
            return payment.stripe_url
        try:
            session = stripe.checkout.Session.create(
                line_items=[
                    {
                        "price_data": {
                            "currency": "usd",
                            "product_data": {"name": "Ticket"},
                            "unit_amount": int(payment.amount * 100),
                        },
                        "quantity": 1,
                    }
                ],
                metadata={"payment_id": str(payment.id)},
                mode="payment",
                success_url="http://localhost:8000/payment/success",
                cancel_url="http://localhost:8000/payment/cancel",
            )
            payment.stripe_session_id = session.id
            payment.stripe_url = session.url
            await self.repo.session.commit()
            return session.url
        except Exception as e:
            print(f"Stripe Error: {e}")
            raise HTTPException(status_code=500, detail="Ошибка при создании платежа")

    async def webhook(self, request: Request, ticket_client: ApiClient):
        payload = await request.body()
        sig_header = request.headers.get("stripe-signature")
        webhook_secret = settings.STRIPE_WEBHOOK_SECRET

        try:
            event = stripe.Webhook.construct_event(payload, sig_header, webhook_secret)
        except stripe.error.SignatureVerificationError:
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={"error": "Invalid signature"},
            )

        session = event["data"]["object"]

        metadata = getattr(session, "metadata", None)
        payment_id_str = getattr(metadata, "payment_id", None) if metadata else None

        if not payment_id_str:
            return {"status": "ignored"}

        payment_id = int(payment_id_str)
        event_type = event["type"]

        try:
            payment = await self.get_payment_by_id(payment_id)
            if payment.status == PaymentStatus.succeeded:
                return
            if event_type == "checkout.session.completed":
                await self.update_payment_status(
                    payment_id, PaymentStatus.succeeded, ticket_client
                )

            elif event_type in [
                "payment_intent.payment_failed",
                "checkout.session.expired",
            ]:
                await self.update_payment_status(
                    payment_id, PaymentStatus.failed, ticket_client
                )

            else:
                return {"status": "ignored", "event": event_type}

        except Exception as e:

            print(f"Error processing webhook: {e}")
            return JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content={"error": "Internal processing error"},
            )

        return {"status": "success"}

    async def update_payment_status(
        self, payment_id: int, payment_status: PaymentStatus, ticket_client: ApiClient
    ) -> PaymentModel:
        if not (
            update_payment := await self.repo.update_payment_status(
                payment_id, payment_status
            )
        ):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Invalid payment data"
            )

        ticket_id = update_payment.ticket_id
        
        if payment_status == PaymentStatus.succeeded:
            await ticket_client.send_payment_success_event(ticket_id)
        elif payment_status == PaymentStatus.failed:
            await ticket_client.send_payment_failed_event(ticket_id)

        return update_payment


    async def send_payment_success_message(ticket_id: int):
        await broker.publish(
            {"ticket_id": ticket_id},
            queue=settings.Payment_Status_Queue
        )
    
    async def _verify_and_map_payment_data(
        self, ticket_details: PaymentCreate, ticket_client: ApiClient, user_id: int
    ) -> PaymentModel:

        ticket = await ticket_client.get_ticket(ticket_details.ticket_id, user_id)
        if not ticket:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Invalid payment data and problem here",
            )

        if user_id != ticket.get("user_id"):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid payment data and problem here2",
            )

        payment = PaymentModel(
            ticket_id=ticket.get("ticket_id"),
            flight_id=ticket.get("flight_id"),
            seat_id=ticket.get("seat_id"),
            user_id=ticket.get("user_id"),
            amount=Decimal(str(ticket.get("price"))),
            payment_method="card",
        )
        await self.repo.create_purchase_intent(payment)
        return payment

    async def check_payment_status(self, payment_id: int):
        payment = await self.get_payment_by_id(payment_id)
        if payment.status == PaymentStatus.succeeded:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT, detail="Ticket already paid"
            )
        elif payment.status == PaymentStatus.pending:
            return