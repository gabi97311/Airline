from src.config_database.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Enum
from datetime import date

from src.enums import ProcessedStatus

class ProcessedEventsModel(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    event_type: Mapped[str]
    aggregate_id: Mapped[int]
    processed_at: Mapped[date]
    status: Mapped[ProcessedStatus] = mapped_column(Enum)