from fastapi import HTTPException,status
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemes.flight_schemes import FlightQuery, FlightCreate
from app.repositories.flight_repositories import FlightRepositories
from app.services.seat_services import SeatServices 
from app.models.airplane_models import Airplane



class FlightServices:
    async def __init__(
        self,
        repository: FlightRepositories,
        seat_service: SeatServices,
        airplane: Airplane,
        session = AsyncSession
        ): 
        
        self.repository = repository
        self.seat_service = seat_service
        self.airplane = airplane
        self.session = self.session
        
        
        
    async def get_flight_list(self, query: FlightQuery):
        return await self.repository.get_flight_list(query)
    
    async def get_flight_by_id(self, flight_id:int):
        if flight:= await self.repository.get_flight_by_id(flight_id):
            return flight
        else: 
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='flight not found')
        
    async def create_flight(self, flight_details: FlightCreate):
        pass 
    

        