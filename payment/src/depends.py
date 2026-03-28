from fastapi import Depends
from typing import Annotated
from src.database import AsyncSessionDep

from src.service import PaymentService
from src.repositories import PaymentRepository

def get_payment_service(session: AsyncSessionDep) -> PaymentService:
    return PaymentService(PaymentRepository(session))

PaymentServiceDep = Annotated[PaymentService, Depends(get_payment_service)]