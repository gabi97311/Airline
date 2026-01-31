import enum
from datetime import date
from sqlalchemy import Enum, Date, Boolean, ForeignKey, Index
from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

# from ..models.users_model import UsersModel

class TripType(enum.Enum):
    one_way = 'one-way'
    round_trip = 'round-trip'
    
class Season(enum.Enum):
    summer = 'summer'
    autumn = 'autumn'
    winter = 'winter'
    spring = 'spring'

class TicketClass(enum.Enum):
    economy = 'economy'
    comfort = 'comfort'
    business = 'business'
    first_class = 'first_class'
    

class TicketModel(Base):
    __tablename__  = 'tickets'
    
    ticket_id: Mapped[int] = mapped_column(primary_key=True)
    
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'),index=True,nullable=False) 
    # user: Mapped["UsersModel"] = relationship(back_populates="tickets")
    
    is_delay: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    year: Mapped[int]
    month: Mapped[int]
    day_of_month: Mapped[int]
    day_of_week: Mapped[int]
    flight_date: Mapped[date]
    
    reporting_airline: Mapped[str]
    origin: Mapped[str]
    origin_state: Mapped[str] = mapped_column(index=True)
    dest:Mapped[str]
    dest_state: Mapped[str] = mapped_column(index=True)
    __table_args__ = (
        Index(
        "ix_origin_dest_state",
        "origin_state",
        "dest_state"
        ),
)
    
    crs_dep_time: Mapped[int]
    
    cancelled: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    diverted: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    
    distance: Mapped[float]
    distance_group: Mapped[int]
    arr_delay: Mapped[float]
    arr_delay_minutes: Mapped[float]
    air_time: Mapped[float]
    
    ticket_class: Mapped[TicketClass] = mapped_column(Enum(TicketClass))
    trip_type: Mapped[TripType] = mapped_column(Enum(TripType))
    price: Mapped[float]
    season: Mapped[Season] = mapped_column(Enum(Season))
    
    