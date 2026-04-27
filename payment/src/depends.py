from fastapi import Depends, Request
from faststream.rabbit import RabbitBroker
from typing import Annotated

from src.api_client import ApiClient
from src.database import AsyncSessionDep
from src.service import PaymentService
from src.repositories import PaymentRepository
from src.config import settings

def get_payment_service(session: AsyncSessionDep) -> PaymentService:
    return PaymentService(PaymentRepository(session))

PaymentServiceDep = Annotated[PaymentService, Depends(get_payment_service)]

def get_ticket_client():
    return ApiClient(base_url= settings.flight_auth_service)    

TicketClientDep = Annotated[ApiClient,Depends(get_ticket_client)]

def get_broker(request: Request) -> RabbitBroker:
    return request.app.state.broker