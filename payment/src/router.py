from fastapi import APIRouter, Depends, HTTPException, Request
from src.depends import PaymentServiceDep, TicketClientDep
from src.schemes import PaymentCreate
from src.jwt import get_current_user_id

router = APIRouter(prefix="/payment", tags=["Payment"])

@router.post("/create_checkout_session")
async def create_checkout_session(
    payment_details: PaymentCreate,
    payment_service: PaymentServiceDep,
    ticket_client: TicketClientDep,
    user_id = Depends(get_current_user_id)
):
    return await payment_service.create_checkout_session(payment_details,ticket_client,user_id)

@router.post("/webhook")
async def stripe_webhook(request: Request, payment_service: PaymentServiceDep):
    return await payment_service.webhook(request)
    
@router.get("/success")
async def payment_success():
    return {"message": "Good"}

@router.get("/cancel")
async def payment_cancel():
    return {"message": "not Good"}
