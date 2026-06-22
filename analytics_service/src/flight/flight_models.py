from src.config_database.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from datetime import date 

class FlightModel(Base):
    __tablename__ = 'analytics_flights'

    flight_id: Mapped[int] = mapped_column(primary_key=True)
    flight_date: Mapped[date]
    reporting_airline: Mapped[str]
    origin: Mapped[str]
    dest: Mapped[str]
    is_delay: Mapped[bool]


class FlightDetailsModel(Base):
    __tablename__ = 'analytics_flight_details'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    flight_id: Mapped[int]

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
