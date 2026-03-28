from fastapi import APIRouter, Depends
from app.schemes.airplane_schemes import AirplaneCreate, AirplaneResponse, AirplaneOptions
from app.depends import AirplaneServiceDep, check_admin_privileges

router = APIRouter(prefix='/airplanes',tags=['Airplane'])

@router.post('/')
async def add_airplane(
    airplane_service:AirplaneServiceDep,
    airplane_details: AirplaneCreate = Depends(),
    admin: dict = Depends(check_admin_privileges)
    ):
    return await airplane_service.create_airplane(airplane_details)

@router.get("/",response_model=list[AirplaneResponse])
async def get_airplane(
    airplane_service: AirplaneServiceDep
): 
    return await airplane_service.get_airplane_list()

@router.get('/options', response_model=list[AirplaneOptions])
async def get_airplane_options(airplane_service: AirplaneServiceDep):
    return await airplane_service.get_airplane_options()