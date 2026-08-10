from app.outboxes.outbox_repositories import OutBoxRepo
from app.outboxes.outbox_scheme import BaseAnalyticsEvent, OutboxEventCreate


class OutBoxService:
    def __init__(self, repo: OutBoxRepo):
        self.repo = repo

    async def save(self, message: BaseAnalyticsEvent):
        outbox_event = OutboxEventCreate(
            id=message.event_id,
            routing_key=message.routing_key,
            payload=message.model_dump(mode='json')
        )
        await self.repo.save(outbox_event)
        