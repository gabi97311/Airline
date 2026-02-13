from fastapi import APIRouter

router = APIRouter(prefix='/ticket', tags=['Ticket'])

@router.get('/list')
def get_ticket_list():
    pass 