import pika 
from src.config import settings

connection_params = pika.ConnectionParameters(
    host=settings.RMQ_HOST, 
    port=settings.RMQ_PORT,
    credentials=pika.PlainCredentials(settings.RMQ_USER, settings.RMQ_PASSWORD)
)

def get_rabbitmq_connection() -> pika.BlockingConnection:
    return pika.BlockingConnection(
        parameters=connection_params
    )