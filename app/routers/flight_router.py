from fastapi import APIRouter, Depends
from app.depends import FlightServiceDep, check_admin_privileges
from app.schemes.flight_schemes import FlightCreate, FlightQuery

router = APIRouter(prefix='/flight', tags=['flight'])

@router.post('/')
async def create_flight(
    flight_service: FlightServiceDep,
    flight_details: FlightCreate = Depends(),
    admin: dict = Depends(check_admin_privileges)):
    return await flight_service.create_flight(flight_details)

@router.get('/')
async def get_flights(flight_service: FlightServiceDep, flight_query: FlightQuery = Depends()):
    return await flight_service.get_flight_list(flight_query)

@router.get('/{flight_id}')
async def get_flight_by_id(flight_id:int, flight_service: FlightServiceDep):
    return await flight_service.get_flight_by_id(flight_id)

@router.put('/{flight_id}')
async def update_flight_by_id(flight_id: int, flight_service: FlightServiceDep):
    pass

@router.delete('/{flight_id}')
async def delete_flight_by_id(flight_id:int, flight_service: FlightServiceDep):
    pass 