from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

# import model
from app.seats.seat_model import Seat, SeatStatus


class SeatRepositories:

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_seat_by_id(self, flight_id:int, seat_id: int):
        stmt = select(Seat).where(Seat.flight_id == flight_id, Seat.seat_id == seat_id)
        result = await self.session.execute(stmt)
        return result.scalars().first()

    async def get_seat_list(self, flight_id: int) -> list[Seat] | None:
        stmt = select(Seat).where(Seat.flight_id == flight_id)
        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def add_seat(self, seat: Seat):
        self.session.add(seat)

    async def get_seat_for_update(self, seat_id: int) -> Seat:
        stmt = select(Seat).where(Seat.seat_id == seat_id).with_for_update()
        seat = await self.session.execute(stmt)
        return seat.scalars().first()

    async def update_seat_status(self, flight_id: int, seat_id: int, status: SeatStatus):
        seat = update(Seat).where(Seat.seat_id == seat_id and Seat.flight_id == flight_id).values(seat_status=status)
        await self.session.execute(seat)
