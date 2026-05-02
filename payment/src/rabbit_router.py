from faststream.rabbit.fastapi import RabbitRouter
from src.config import settings

rabbit_router = RabbitRouter(settings.RMQ_URL)
