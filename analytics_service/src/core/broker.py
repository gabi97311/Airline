from faststream.rabbit import RabbitBroker

from src.core.config import settings
from src.flights import router as flight_router

main_broker = RabbitBroker(url=settings.RMQ_URL)

main_broker.include_router(flight_router)