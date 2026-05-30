from sqlalchemy.ext.asyncio import AsyncSession

from src.flight.flight_models import AnalyticsFlight, AnalyticsFlightDetails

class FlightRepo:
    def __init__(self, session: AsyncSession):
        self.session = session
        
    async def get_flight(self, flight_id: int) -> AnalyticsFlight | None:
        stmt = await self.session.get(AnalyticsFlight, flight_id)
        return stmt
    
    async def add_flights(self, flight:AnalyticsFlight) -> None:
        self.session.add(flight)
        await self.session.commit()