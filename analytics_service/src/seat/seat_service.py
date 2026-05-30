from sqlalchemy.ext.asyncio import AsyncSession

from src.seat.seat_repo import SeatRepo
from src.seat.seat_models import AnalyticsSeat
from .seat_scheme import SeatScheme

class SeatService:
    def __init__(self, session: AsyncSession, seat_repo: SeatRepo):
        self.session = session
        self.repo = seat_repo 
    async def add_seats(self, seats: list[SeatScheme]):
        if not seats:
            return False