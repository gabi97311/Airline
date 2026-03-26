from app.database import Base
from sqlalchemy.orm import Mapped,mapped_column,relationship
from sqlalchemy import String
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from .flight_models import Flight    

class Airplane(Base): 
    __tablename__ = 'airplanes'
    
    airplane_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    model_name: Mapped[str] = mapped_column(String(50), unique=True)
    
    max_seats: Mapped[int] = mapped_column(default=30)
    seats_config: Mapped[str] = mapped_column(String(10), default="ABCDEF")
    
    flights: Mapped[list["Flight"]] = relationship(back_populates="airplane")