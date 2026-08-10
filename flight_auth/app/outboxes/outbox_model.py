import uuid
from datetime import datetime
from sqlalchemy import String, DateTime, func, Boolean
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import mapped_column, Mapped

from app.core import Base

class OutBox(Base):
    id: Mapped[uuid.UUID] = mapped_column( UUID(as_uuid=True), primary_key=True, default=uuid.uuid4 )
    event_type: Mapped[str] = mapped_column(String, nullable=False)
    routing_key: Mapped[str] = mapped_column(String, nullable=False)
    payload: Mapped[dict] = mapped_column(JSONB, nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now()
    )
    published: Mapped[bool] = mapped_column(Boolean, default=False, server_default="false")
