from pydantic import BaseModel, ConfigDict

from app.seats.seat_schemes import SeatClass, SeatStatus

class SeatShemes(BaseModel):
    seat_code: str 
    seat_class: SeatClass
    price: float
    
class SeatCreate(BaseModel):
    flight_id:int
    seat_code:str
    seat_class: SeatClass
    price: float
    seat_status: SeatStatus 
    
    model_config = ConfigDict(from_attributes=True)
    
class SeatResponse(BaseModel):
    seat_id: int
    seat_code: str 
    seat_class: SeatClass
    price: float
    seat_status: SeatStatus
    
    model_config = ConfigDict(from_attributes=True)
