from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from src.seat.seat_models import AnalyticsSeat as Seat
class SeatRepo:
    def __init__(self, session: AsyncSession):
        self.session = session
        
    async def add_seats(self, seats: list[Seat]) -> None:
        self.session.add_all(seats)
        
    async def get_seat(self, flight_id:int):
        stmt = select(Seat).where(Seat.flight_id == flight_id)
        result = await self.session.execute(stmt)
        return result.scalars().first()