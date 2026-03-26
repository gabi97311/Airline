from fastapi import APIRouter
from app.depends import SeatServiceDep
from app.schemes.seat_schemes import SeatResponse
router = APIRouter(prefix='/seats', tags=['Seat'])

@router.get('/', response_model = list[SeatResponse])
async def get_seat_list(flight_id:int,seat_service: SeatServiceDep):
    return await seat_service.get_seat_list(flight_id)
