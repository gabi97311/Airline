from fastapi import HTTPException,status
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemes.flight_schemes import FlightQuery, FlightCreate
from app.services.seat_services import SeatServices 
from app.services.airplane_service import AirplaneServices

from app.models.flight_models import Flight

from app.repositories.flight_repositories import FlightRepositories


class FlightServices:
    def __init__(
        self,
        session: AsyncSession,
        repository: FlightRepositories,
        seat_service: SeatServices,
        airplane_service:AirplaneServices
        ): 
        
        self.repository = repository
        self.seat_service = seat_service
        self.airplane_service = airplane_service
        self.session = session
        
        
    async def get_flight_list(self, flight_query: FlightQuery):
        return await self.repository.get_flight_list(flight_query)
    
    async def get_flight_by_id(self, flight_id:int) -> Flight:
        if flight:= await self.repository.get_flight_by_id(flight_id):
            return flight
        else: 
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='flight not found')
        
    async def create_flight(self, flight_details: FlightCreate):
        
        if not (airplane := await self.airplane_service.get_airplane_by_id(flight_details.airplane_id)):
            raise HTTPException(status_code=404, detail='Airplane not found')
        
        flight = Flight(**flight_details.model_dump())
        
        try: 
            await self.repository.create_flight(flight)
            await self.seat_service.generate_seats_for_flight(flight.flight_id, airplane) 
            await self.session.commit()
            await self.session.refresh(flight)
            return flight
        except Exception as e: 
            await self.session.rollback()
            raise e 
        
    

        