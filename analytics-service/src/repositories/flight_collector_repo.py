from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
class FlightCollectorRepo: 
    def __init__(self, session: AsyncSession):
        self.session = session
        
    async def get_all_data(self):
        stmt = select()