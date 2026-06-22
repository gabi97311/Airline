from pydantic import BaseModel
from datetime import date


class FlightScheme(BaseModel):
    flight_id: int
    flight_date: date
    reporting_airline: str
    origin: str
    dest: str
    is_delay: bool

    class Config:
        from_attributes = True
        
class FlightDetailsScheme(BaseModel):
    id: int
    flight_id: int

    year: int
    month: int
    day_of_month: int
    origin_state: str
    dest_state: str
    crs_dep_time: int
    cancelled: bool
    diverted: bool
    distance: float
    distance_group: int
    arr_delay: float
    arr_delay_minutes: float
    air_time: float

    class Config:
        from_attributes = True