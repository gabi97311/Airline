from app.services import FlightServices, SeatServices, TicketServices
from app.repositories.analytics_repositories import AnalyticsRepository

class AnalyticsServices:
    def _init_(self,analytics_repo:AnalyticsRepository):
        self.analytics_repo = analytics_repo
    
    async def get_flight_by_id(self, flight_id: int):
        return self.analytics_repo
        
    async def get_full_flight_data(self):
        return self.analytics_repo.get_full_data()
    