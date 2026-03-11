from sqlalchemy.orm import Session
from sqlalchemy import select

import pandas as pd

from app.repositories.seat_repositories import SeatRepositories
from app.repositories.airplane_repositories import AirplaneRepositories as Airplane
class SeatServices:
    def __init__(self,session: Session, seat_repo: SeatRepositories):
        self.session = session

        self.seat_repo = seat_repo
    
    def get_seat_list(self, flight_id: int):
        pass
        
    def generate_seats_for_flight(self,flight_id: int, airplane: Airplane):
        pass
    
    def _build_seat_dataframe():
        pass