from src.config_database import settings
from faststream.rabbit.fastapi import RabbitRouter
from faststream.rabbit import Rabbit
router = RabbitRouter(url = 'amqp://guest:guest@rabbitmq:5672/')

@router.subscriber()
