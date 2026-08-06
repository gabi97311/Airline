from app.core.config import settings
from faststream.rabbit import RabbitBroker

from app.tickets import broker_router as ticket_router

main_broker = RabbitBroker(url=settings.RMQ_URL)

main_broker.include_router(ticket_router)
