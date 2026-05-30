from pydantic import BaseModel, ConfigDict
from src.analtics_enum import SeatClass, SeatStatus

class SeatScheme(BaseModel):
    id: int
    flight_id: int
    seat_class: SeatClass
    seat_status: SeatStatus
    price: float    
    model_config = ConfigDict(from_attributes=True)