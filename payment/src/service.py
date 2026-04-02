from decimal import Decimal

import httpx
from fastapi import Depends, HTTPException, status
from typing import Optional, Any


from src.models import PaymentModel
from src.repositories import PaymentRepository
from src.schemes import PaymentCreate
from src.api_client import ApiClient


class PaymentService:
    def __init__(self, repo: PaymentRepository):
        self.repo = repo

    async def create_purchase_intent(
        self, payment_details: PaymentCreate, user_id: int, ticket_client: ApiClient
    ):

        ticket = await ticket_client.get_ticket(payment_details.ticket_id)
        if not ticket:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail="Invalid payment data 1"
            )

        if payment_details.flight_id != ticket.get("flight_id") or \
           payment_details.seat_id != ticket.get("seat_id"):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail="Invalid payment data 2"
            )

        payment = PaymentModel(
            ticket_id = ticket.get('ticket_id'),
            flight_id = ticket.get('flight_id'), 
            seat_id = ticket.get('seat_id'),
            user_id = user_id,
            amount = Decimal(str(ticket.get('price'))),
            payment_method = 'card'
        )
        await self.repo.create_purchase_intent(payment)
        return {'message' : "Good"}
        
    async def get_payment(self):
        pass
