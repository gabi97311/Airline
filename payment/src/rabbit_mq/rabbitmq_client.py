import json
import pika
 
from src.config import settings
class AirlineMQClient:
    def __init__ (self, host: str = settings.RMQ_HOST):
        self.host = host
        self.connection = None
        self.chennel = None
        
    def connect(self):
        if not self.connection or self.connection.is_closed:
            self.connection = pika.BlockingConnection(
                pika.ConnectionParameters(host=self.host)
            )
            self.channel = self.connection.channel()
        return self
    
    def publish(self, queue_name: str, message: dict):
        if not self.channel:
            self.connect()

        self.channel.queue_declare(queue=queue_name, durable=True)
        body = json.dumps(message).encode('utf-8')

        self.channel.basic_publish(
            exchange='',
            routing_key=queue_name,
            body=body,
            properties=pika.BasicProperties(
                delivery_mode=2,
                content_type='application/json'
            )
        )
        
    def close(self):
        if self.connection and not self.connection.is_closed:
            self.connection.close()
            
    def __enter__(self):
        return self.connect()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()