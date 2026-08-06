from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional


class TicketBase(BaseModel):
    passenger_name: str


class TicketCreate(TicketBase):
    seat_id: int
    flight_id: int


class TicketResponse(TicketBase):
    ticket_id: int
    user_id: int
    seat_id: int
    flight_id: int
    price: float
    purchase_time: datetime

    model_config = ConfigDict(from_attributes=True)


class TicketDetailResponse(TicketResponse):
    pass
