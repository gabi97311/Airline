from sqlalchemy.ext.asyncio import AsyncSession 

from src.flight.flight_repo import FlightRepo
from src.flight.flight_models import AnalyticsFlight, AnalyticsFlightDetails

class FlightService:
    def __init__(self, session: AsyncSession, flight_repo:FlightRepo):
        self.session: AsyncSession
        self.repo = flight_repo
    
    async def add_flight(self, flight:dict):
        
        if not self.repo.get_flight():
            pass 
        