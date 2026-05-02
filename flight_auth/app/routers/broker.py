from faststream.rabbit import RabbitExchange, RabbitQueue
from faststream.rabbit.fastapi import RabbitRouter
from app.depends import TicketServiceDep
from app.models.ticket_model import TicketStatus
from app.config import settings

router = RabbitRouter(url=settings.RMQ_URL)

ticket_exchange = RabbitExchange('payment', durable=True)
ticket_queue_succeeded = RabbitQueue('payment_queue_succeeded', routing_key='succeeded')
ticket_queue_failed = RabbitQueue('payment_queue_failed',routing_key='failed')

@router.subscriber(queue=ticket_queue_succeeded, exchange=ticket_exchange)
async def confirm_ticket_payment(ticket_id:int, ticket_service: TicketServiceDep):
    return await ticket_service.change_ticket_status(ticket_id, TicketStatus.paid)

@router.subscriber(queue=ticket_queue_failed, exchange=ticket_exchange)
async def cancel_ticket_payment(ticket_id:int, ticket_service: TicketServiceDep): 
    return await ticket_service.change_ticket_status(ticket_id, TicketStatus.failed)