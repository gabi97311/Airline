from fastapi import APIRouter

from faststream.rabbit.fastapi import RabbitRouter, RabbitBroker
from faststream.rabbit import RabbitExchange
from src.config import settings
from pydantic import BaseModel
from enum import Enum
from fastapi import Depends
from src.broker import router

from src.schemes import PaymentStatusEvent
from src.depends import PaymentServiceDep
test_router = APIRouter(prefix='/test', tags=['Test Router'])
rabbit_router = RabbitRouter(url=settings.RMQ_URL)
# payment_exchange = RabbitExchange('payment')

# class ticket_status(str, Enum):
#     pending = 'pending'
#     succeeded = 'succeeded'
#     failed = 'failed'

# class ticketmodel(BaseModel):
#     id: int
#     ticket_status: ticket_status
    
# ticket_publisher = router.broker.publisher(
#     queue=settings.payment_queue,
#     exchange=payment_exchange
# )

# async def check_ticket(ticket_id: int):
#     pass

# @test_router.post('/ticket_id')
# async def publish_ticket(ticket: ticketmodel):
#     await ticket_publisher.publish(message=ticket.model_dump())
#     return {"status": "Message sent to RabbitMQ"}

@test_router.post('/test')
async def test(ticket: PaymentStatusEvent, payment_service: PaymentServiceDep):
    return await payment_service.send_payment_event(ticket)