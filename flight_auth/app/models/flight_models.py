from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import date
from sqlalchemy import ForeignKey
from typing import List, TYPE_CHECKING
from app.database import Base


if TYPE_CHECKING:
    from .seat_model import Seat
    from .ticket_model import Ticket
    from .airplane_models import Airplane

class Flight(Base): 
    __tablename__ = 'flights'
    
    flight_id : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    flight_date: Mapped[date]
    reporting_airline: Mapped[str]
    origin: Mapped[str]
    dest: Mapped[str]
    airplane_id: Mapped[int] = mapped_column(ForeignKey('airplanes.airplane_id'))
    is_delay: Mapped[bool] = mapped_column(default=False, server_default="False")
    
    airplane: Mapped["Airplane"] = relationship(back_populates="flights")
    seats: Mapped[List["Seat"]] = relationship(back_populates="flight", lazy="select")
    tickets: Mapped[List['Ticket']] = relationship(back_populates='flight')
    details: Mapped["FlightDetails"] = relationship(back_populates='flight')

class FlightDetails(Base): 
    __tablename__ = 'flight_details'
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    flight: Mapped['Flight'] = relationship(back_populates='details')
    flight_id: Mapped[int] = mapped_column(ForeignKey('flights.flight_id'))
    
    year: Mapped[int]
    month: Mapped[int]
    day_of_month: Mapped[int]
    origin_state: Mapped[str]
    dest_state: Mapped[str]
    crs_dep_time: Mapped[int]
    cancelled: Mapped[bool]
    diverted: Mapped[bool]
    distance: Mapped[float]
    distance_group: Mapped[int]
    arr_delay: Mapped[float] 
    arr_delay_minutes: Mapped[float]
    air_time: Mapped[float]
    