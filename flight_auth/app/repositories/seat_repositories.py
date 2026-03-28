from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession 

# import model
from app.models.seat_model import Seat as fs, SeatStatus

class SeatRepositories:
    
    def __init__(self,session:AsyncSession):
        self.session = session
    
    async def get_seat_by_id(self, seat_id:int): 
        return await self.session.get(fs,seat_id)
            
    async def get_seat_list(self, flight_id: int) -> list[fs] | None: 
        stmt = select(fs).where(fs.flight_id == flight_id)
        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def add_seat(self, seat:fs):
        self.session.add(seat)

    async def get_seat_for_update(self, seat_id:int):
        stmt = select(fs).where(fs.seat_id == seat_id).with_for_update()
        return await self.session.execute(stmt).scalar_one_or_none()
    
    async def update_seat_status(self,seat_id: int, status: SeatStatus):
        seat = (update(fs).where(fs.seat_id == seat_id).values(seat_status = status))
        await self.session.execute(seat)
    
    