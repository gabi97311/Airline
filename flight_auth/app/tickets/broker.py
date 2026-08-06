from faststream.rabbit.fastapi import RabbitRouter
from faststream.rabbit import RabbitExchange, RabbitQueue

from app.utils import Services
from app.tickets.ticket_model import TicketStatus

from app.core import settings

router = RabbitRouter()

ticket_exchange = RabbitExchange('payment', durable=True)
ticket_queue_succeeded = RabbitQueue('payment_queue_succeeded', routing_key='succeeded')
ticket_queue_failed = RabbitQueue('payment_queue_failed',routing_key='failed')

@router.subscriber(queue=ticket_queue_succeeded, exchange=ticket_exchange)
async def confirm_ticket_payment(ticket_id:int, service: Services):
    return await service.ticket.change_ticket_status(ticket_id, TicketStatus.paid)

@router.subscriber(queue=ticket_queue_failed, exchange=ticket_exchange)
async def cancel_ticket_payment(ticket_id:int, service: Services): 
    return await service.ticket.change_ticket_status(ticket_id, TicketStatus.failed)
