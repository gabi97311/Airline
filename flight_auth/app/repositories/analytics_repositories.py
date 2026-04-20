from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Flight, FlightDetails , Seat, Ticket
class AnalyticsRepository:
    def __init__(self, session: AsyncSession):
        self.session = session
        
    async def get_full_data(self):
        stmt = select(Flight).join(FlightDetails).join(Seat).join(Ticket)
        result = await self.session.execute(stmt)
        return result.mappings()