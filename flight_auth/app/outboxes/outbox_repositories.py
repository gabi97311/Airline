from sqlalchemy.ext.asyncio import AsyncSession
from app.outboxes.outbox_model import OutBox
from app.flights import FlightAnalyticsMessage
from app.outboxes.outbox_scheme import OutboxEventCreate

class OutBoxRepo:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def save(self, event: OutboxEventCreate):
        outbox = OutBox(**event.model_dump())
        self.session.add(outbox)