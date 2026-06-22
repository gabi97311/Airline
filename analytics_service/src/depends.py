from typing import Annotated
from fastapi import Depends

from src.config_database import AsyncSessionDep
from src.flight import FlightRepo, FlightService
from src.payment import PaymenyRepo, PaymenytService
from src.seat import SeatRepo, SeatService
from src.processing_logs import ProcessedEventRepo, ProcessedEventService


def get_flight_service(session: AsyncSessionDep, payment_service: SeatServiceDep, seat_service: PaymentServiceDep) -> FlightService:
    flight_repo = FlightRepo(session)
    return FlightService(session, flight_repo, payment_service, seat_service)

def get_seat_service(session: AsyncSessionDep) -> SeatService:
    return SeatService(SeatRepo(session))

def get_payment_service(session: AsyncSessionDep) -> PaymenytService:
    return PaymenytService(PaymenyRepo(session))

def get_processed_service(session: AsyncSessionDep) -> ProcessedEventService:
    return ProcessedEventService(ProcessedEventRepo(session))

ProcessedServiceDep = Annotated[ProcessedEventService, Depends(get_processed_service)]
SeatServiceDep = Annotated[SeatService, Depends(get_seat_service)]
PaymentServiceDep = Annotated[PaymenytService, Depends(get_payment_service)]
FlightServiceDep = Annotated[FlightService, Depends(get_flight_service)]