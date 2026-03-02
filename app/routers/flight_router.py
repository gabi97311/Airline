from fastapi import APIRouter, Depends

from app.depends import FlightServiceDep, check_admin_privileges
from app.schemes.flight_schemes import FlightCreate

router = APIRouter(prefix='/flight', tags=['flight'])

@router.post('/create_flight')
def create_flight(flight_service: FlightServiceDep, flight_details: FlightCreate = Depends(), admin: dict = Depends(check_admin_privileges)):
    print(f"Рейс создает админ: {admin.get('sub')}")
    return flight_service.create_flight()