import uuid
from typing import Any
from pydantic import BaseModel
from datetime import datetime, date 


class BaseAnalyticsEvent(BaseModel):
    event_id: str
    routing_key: str
    event_time: datetime
    version: int

class FlightAnalyticsMessage(BaseAnalyticsEvent):
    flight_id: int
    flight_date: date
    reporting_airline: str
    origin: str
    dest: str
    is_delay: bool
    cancelled: bool

class TicketAnalyticsMessage(BaseAnalyticsEvent):
    ticket_id: int
    flight_id: int
    status: str
    price: float
    origin: str
    dest: str
    seat_class: str
    purchase_time: datetime
    flight_time: datetime

class OutboxEventCreate(BaseModel):
    id: uuid.UUID
    routing_key: str
    payload: dict[str, Any]