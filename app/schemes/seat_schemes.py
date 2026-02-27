from pydantic import BaseModel, ConfigDict

from app.models.seat_model import SeatClass, SeatStatus, TripType

class SeatShemes(BaseModel):
    seat_code: str 
    seat_class: SeatClass
    price: float
    trip_type: TripType
    
class SeatResponse(SeatShemes):
    seat_id: int
    seat_status: SeatStatus
    
    model_config = ConfigDict(from_attributes=True)
