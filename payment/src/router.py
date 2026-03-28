from fastapi import APIRouter, Depends, HTTPException
from src.depends import PaymentServiceDep
from src.schemes import PaymentSchemes 
from src.jwt import get_current_user_id

router = APIRouter(prefix='/payment', tags= ['Payment'])

@router.post('/purchase')
async def create_purchase_intent(
    payment_service: PaymentServiceDep,
    payment_details: PaymentSchemes = Depends(),
    user_id = Depends(get_current_user_id),
    ):
    return await payment_service.create_purchase_intent(payment_details, user_id)