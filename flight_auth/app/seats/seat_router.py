from fastapi import APIRouter

from app.utils import Services
from app.seats.seat_schemes import SeatResponse

router = APIRouter(prefix="/seats", tags=["Seat"])


@router.get("/", response_model=list[SeatResponse])
async def get_seat_list(flight_id: int, services: Services):
    return await services.seat.get_seat_list(flight_id)


@router.get("/{seat_id}", response_model=SeatResponse)
async def get_seat_by_id(flight_id: int, seat_id: int, services: Services):
    return await services.seat.get_seat_by_id(flight_id, seat_id)
