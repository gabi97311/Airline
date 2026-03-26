from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, func
from datetime import datetime
from typing import TYPE_CHECKING

from app.database import Base

if TYPE_CHECKING:
    from app.models.flight_models import Flight
    from app.models.users_model import UsersModel 
    from app.models.seat_model import Seat
    
    

class Ticket(Base):
    
    __tablename__ = 'tickets'
    
    ticket_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    user: Mapped['UsersModel'] = relationship(back_populates='tickets')
    
    seat_id: Mapped[int] = mapped_column(ForeignKey('seats.seat_id'))
    seat: Mapped["Seat"] = relationship(back_populates='ticket')
    
    flight_id: Mapped[int] = mapped_column(ForeignKey('flights.flight_id'))
    flight: Mapped["Flight"] = relationship(back_populates="tickets")
    
    passenger_name: Mapped[str]
    
    purchase_time: Mapped[datetime] = mapped_column(server_default=func.now())
    
    flight_time: Mapped[datetime]
    
    price: Mapped[float]