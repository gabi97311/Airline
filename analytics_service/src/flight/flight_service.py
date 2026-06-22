from sqlalchemy.ext.asyncio import AsyncSession

from src.flight import FlightRepo, FlightScheme
from src.payment import PaymenytService
from src.seat import SeatService


class FlightService:
    def __init__(
        self,
        session: AsyncSession,
        flight_repo: FlightRepo,
        payment_service: PaymenytService,
        seat_service: SeatService,
    ):
        self.session = session,
        self.repo = flight_repo
        self.payment = payment_service, 
        self.seat = seat_service

    async def add_flight(self, flight: FlightScheme):
        pass
