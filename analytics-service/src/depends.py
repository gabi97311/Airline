from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.config_database.database import AsyncSessionDep,FlightSessionDep, PaySessionDep
from src.services import FlightService, PaymentService, FlightCollector
from src.repositories import FlightRepository, PaymentRepository, FlightCollectorRepo


def get_flight_collector_service(session: FlightSessionDep) -> FlightCollector: 
    return FlightCollector(FlightCollectorRepo(session))

def get_flight_service(session: AsyncSessionDep ) -> FlightService:
    return FlightService(FlightRepository(session))

FlightServiceDep = Annotated[FlightService, Depends(get_flight_service)]
FlightCollectorDep = Annotated[FlightCollector, Depends(get_flight_collector_service)]