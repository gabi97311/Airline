from enum import Enum

class RabbitExchange(str, Enum):
    FLIGHT_EVENTS = "flight_events"
    PAYMENT_EVENTS = "payment_events"

class FlightEvent(str, Enum):
    CREATED = "flight.created"
    UPDATED = "flight.updated"
    COMPLETED = "flight.completed"
    CANCELLED = "flight.cancelled"
    DELAYED = "flight.delayed"

class TicketEventType(str, Enum):
    CREATED = "ticket.created"
    PAID = "ticket.paid"
    REFUNDED = "ticket.refunded"
    CANCELLED = "ticket.cancelled"


class SeatClass(str, Enum):
    economy = 'Economy'
    business = 'Business'
    comfort = 'Comfort'
    first = 'First'
    
class SeatStatus(str, Enum):
    free = 'Free'
    pending = 'Pending'
    occupied = 'Occupied'
    blocked = 'Blocked'

class TicketStatus(str, Enum):
    paid = "paid"
    pending = "pending"
    failed = "failed"
    