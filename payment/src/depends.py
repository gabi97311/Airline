from fastapi import Depends
from typing import Annotated

from src.api_client import ApiClient
from src.database import AsyncSessionDep
from src.service import PaymentService
from src.repositories import PaymentRepository
from src.broker import router 
from src.config import settings

def get_payment_service(session: AsyncSessionDep) -> PaymentService:
    return PaymentService(repo = PaymentRepository(session), broker=router.broker)

PaymentServiceDep = Annotated[PaymentService, Depends(get_payment_service)]

def get_ticket_client():
    return ApiClient(base_url= settings.flight_auth_service)    

TicketClientDep = Annotated[ApiClient,Depends(get_ticket_client)]

