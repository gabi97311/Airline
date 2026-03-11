from fastapi import HTTPException,status

from app.schemes.flight_schemes import FlightQuery, FlightCreate
from app.repositories.flight_repositories import FlightRepositories
from app.services.seat_services import SeatServices 
from app.models.airplane_models import Airplane



class FlightServices:
    def __init__(self, repository: FlightRepositories, seat_service: SeatServices, airplane: Airplane): 
        self.repository = repository
        self.session = repository.session
        self.seat_service = seat_service
        self.airplane = airplane
        
        
        
    def get_flight_list(self, query: FlightQuery):
        return self.repository.get_flight_list(query)
    
    def get_flight_by_id(self, flight_id:int):
        if flight:= self.repository.get_flight_by_id(flight_id):
            return flight
        else: 
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='flight not found')
    
    def create_flight(self,flight_details: FlightCreate, airplane_id: int):
        # if self.airplane.
        try:
            flight = self.repository.create_flight(flight_details)
            if not flight:
                raise ValueError("Couldn't create flight in the database")
            self.seat_service.generate_seats_for_flight(flight.flight_id)
        except Exception as e:
            self.session.rollback()
            raise e
        