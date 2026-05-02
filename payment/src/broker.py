from faststream.rabbit.fastapi import RabbitRouter
from src.config import settings

router = RabbitRouter(url=settings.RMQ_URL, prefix="/payment", tags=["Payment"])