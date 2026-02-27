from fastapi import APIRouter

router = APIRouter(prefix='/seat', tags=['Seat'])

@router.get('get_seat_list')
def get_seat_list():
    return 'hello'