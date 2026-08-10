from fastapi import APIRouter, Depends
from app.utils import Services, Jwt
from app.utils import Services
from app.flights.flight_schemes import FlightCreate, FlightQuery, FlightUpdate 

router = APIRouter(prefix='/flight', tags=['flight'])

@router.post('/')
async def create_flight(
    services: Services,
    flight_details: FlightCreate = Depends(),
    admin: dict = Depends(Jwt.check_admin_privileges)):
    return await services.flight.create_flight(flight_details)

@router.get('/')
async def get_flights(services: Services, flight_query: FlightQuery = Depends()):
    return await services.flight.get_flight_list(flight_query)

@router.get('/{flight_id}')
async def get_flight_by_id(flight_id:int, services: Services):
    return await services.flight.get_flight_by_id(flight_id)

@router.put('/{flight_id}')
async def update_flight_by_id(services: Services, flight: FlightUpdate = Depends()):
    # return await services.flight.update_flight_by_id() 
    pass

@router.delete('/{flight_id}')
async def delete_flight_by_id(flight_id:int, services: Services):
    pass 