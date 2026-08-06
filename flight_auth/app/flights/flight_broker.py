from faststream.rabbit.fastapi import RabbitRouter
from enum import Enum

router = RabbitRouter()

class RabbitExchange(str, Enum):
    FLIGHT_EVENTS = "flight_events"
    PAYMENT_EVENTS = "payment_events"