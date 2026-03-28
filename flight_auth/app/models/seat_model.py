from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey,Enum
import enum
from typing import TYPE_CHECKING

from app.database import Base


if TYPE_CHECKING: 
    from app.models.flight_models import Flight
    from app.models.ticket_model import Ticket
    
class SeatClass(str, enum.Enum):
    economy = 'Economy'
    business = 'Business'
    comfort = 'Comfort'
    first = 'First'
    
class SeatStatus(str, enum.Enum):
    free = 'Free'
    occupied = 'Occupied'
    booked = 'Booked'
    blocked = 'Blocked'
    
    
class Seat(Base): 
    
    __tablename__ = 'seats'
    
    seat_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    
    flight_id: Mapped[int] = mapped_column(ForeignKey('flights.flight_id'))
    flight: Mapped["Flight"] = relationship(back_populates="seats")
    
    ticket: Mapped['Ticket'] = relationship(back_populates='seat')
    
    seat_code: Mapped[str]
    seat_class: Mapped[SeatClass] = mapped_column(
        Enum(
            SeatClass, 
            name='seat_class', 
            values_callable=lambda obj: [e.value for e in obj]
        ), 
        default=SeatClass.economy, 
        server_default="Economy"
    )
    price: Mapped[float]
    seat_status: Mapped[SeatStatus] = mapped_column( 
        Enum(
            SeatStatus, 
            name='seat_status',
            # Эта строка заставляет брать 'Free' вместо 'free'
            values_callable=lambda obj: [e.value for e in obj]
        ),
        default=SeatStatus.free, 
        server_default="Free"
    )
    