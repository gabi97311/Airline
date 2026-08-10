from faststream.rabbit.fastapi import RabbitRouter
from faststream.rabbit import RabbitExchange, RabbitQueue

router = RabbitRouter()

@router.subscriber(queue='flight_create', exchange=  )