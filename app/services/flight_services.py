from fastapi import HTTPException,status

from app.repositories.flight_repositories import FlightRepositories
from app.schemes.flight_schemes import FlightQuery
from app.schemes.user_schemes import UserResponse

class FlightServices:
    def __init__(self,flight_repo: FlightRepositories): 
        self.flight_repo = flight_repo
        
    def get_flight_list(self, query: FlightQuery):
        return self.flight_repo.get_flight_list(query)
    
    def get_flight_by_id(self, flight_id:int):
        if flight:= self.flight_repo.get_flight_by_id(flight_id):
            return flight
        else: 
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='flight not found')
    
