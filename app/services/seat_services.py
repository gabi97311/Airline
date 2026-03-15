from sqlalchemy.ext.asyncio import AsyncSession 

import numpy as np

from app.models.seat_model import Seat
from app.models.airplane_models import Airplane
from app.schemes.seat_schemes import SeatClass, SeatStatus

from app.repositories.seat_repositories import SeatRepositories

class SeatServices:
    def __init__(self,session: AsyncSession, seat_repo: SeatRepositories):
        self.session = session
        self.seat_repo = seat_repo

    async def get_seat_list(self, flight_id: int):
        seats = await self.seat_repo.get_seat_list(flight_id)
        return seats
        
    async def generate_seats_for_flight(self, flight_id: int, airplane: Airplane):
        seats_data_list = self._build_seat_dataframe(flight_id, airplane)
        try:
           for seat_dict in seats_data_list:
            seat = Seat(**seat_dict)
            await self.seat_repo.add_seat(seat)
        except Exception as e: 
            await self.session.rollback()
            raise e
    
    def _build_seat_dataframe(self,flight_id:int ,airplane: Airplane):
        max_seat = airplane.max_seats
        default_price = np.random.randint(45,55)
        letters = ['A','B','C','D','E','F']
        seat_data = []
        seat_count = 0
        
        seat_class = [
            (SeatClass.economy, 40, 1.0),
            (SeatClass.comfort, 30, 1.5),
            (SeatClass.business, 20, 3),
            (SeatClass.first, 10, 5)
        ]
        
        for s_class, shape, multiplier in seat_class:
            class_limit = int(max_seat * shape)
            for _ in range(class_limit):
                if seat_count > max_seat: 
                    break
                
                row = (seat_count // len(letters)) + 1
                letter = (seat_count % len(letters))
                
                seat_data.append({
                    'flight_id': flight_id,
                    'seat_code': f"{row}{letter}",
                    'seat_class': s_class,
                    'price': float(default_price * multiplier),
                    'seat_status': SeatStatus.free
                })
                seat_count +=1
                
        while seat_count < max_seat:
            row = (seat_count // len(letters)) + 1
            letter = (seat_count % len(letters))
                
            seat_data.append({
                'flight_id': flight_id,
                'seat_code': f"{row}{letter}",
                'seat_class': s_class,
                'price': float(default_price * multiplier),
                'seat_status': SeatStatus.free
            })
            seat_count +=1
            
        return seat_data