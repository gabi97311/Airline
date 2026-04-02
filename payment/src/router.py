from fastapi import APIRouter, Depends, HTTPException
from src.depends import PaymentServiceDep, TicketClientDep
from src.schemes import PaymentSchemes
from src.jwt import get_current_user_id

router = APIRouter(prefix="/payment", tags=["Payment"])


@router.post("/purchase")
async def create_purchase_intent(
    payment_service: PaymentServiceDep,
    ticket_client: TicketClientDep,
    payment_details: PaymentSchemes = Depends(),
    user_id=Depends(get_current_user_id),
):
    return await payment_service.create_purchase_intent(
        payment_details, user_id, ticket_client
    )
