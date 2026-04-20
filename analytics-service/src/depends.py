from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.config_database.database import AsyncSessionDep
from src.services import FlightService, PaymentService
from src.repositories import FlightRepository, PaymentRepository

def get_flight_service(session: AsyncSessionDep ) -> FlightService:
    return FlightService(FlightRepository(session))

FlightServiceDep = Annotated[FlightService, Depends(get_flight_service)]