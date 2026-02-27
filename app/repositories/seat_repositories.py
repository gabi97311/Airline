from sqlalchemy import select, update
from sqlalchemy.orm import Session

# import model
from app.models.seat_model import FlightSeat as fs, SeatStatus

class SeatRepositories:
    
    def __init__(self,session:Session):
        self.session = session
        
    def commit(self):
        self.session.commit()
    
    def get_seat_by_id(self, seat_id:int): 
        return self.session.get(fs,seat_id)
            
    def get_seat_list(self, flight_id: int) -> list[fs] | None: 
        stmt = select(fs).where(fs.flight_id == flight_id)
        return self.session.execute(stmt).scalars().all()

    def get_seat_for_update(self, seat_id:int):
        stmt = select(fs).where(fs.seat_id == seat_id).with_for_update()
        return self.session.execute(stmt).scalar_one_or_none()
    
    def update_seat_status(self,seat_id: int, status: SeatStatus):
        seat = (update(fs).where(fs.seat_id == seat_id).values(seat_status = status))
        self.session.execute(seat)
    