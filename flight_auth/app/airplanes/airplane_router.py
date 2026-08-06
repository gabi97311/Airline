from fastapi import APIRouter, Depends
from app.airplanes.airplane_schemes import AirplaneCreate, AirplaneResponse, AirplaneOptions
from app.utils import Jwt, Services

router = APIRouter(prefix='/airplanes',tags=['Airplane'])

@router.post('/')
async def add_airplane(
    services:Services,
    airplane_details: AirplaneCreate = Depends(),
    admin: dict = Depends(Jwt.check_admin_privileges)
    ):
    return await services.airplane.create_airplane(airplane_details)

@router.get("/",response_model=list[AirplaneResponse])
async def get_airplane(
    services: Services
): 
    return await services.airplane.get_airplane_list()

@router.get('/options', response_model=list[AirplaneOptions])
async def get_airplane_options(services: Services):
    return await services.airplane.get_airplane_options()