from fastapi import APIRouter, Depends
from app.schemes.airplane_schemes import AirplaneCreate, AirplaneResponse 
from app.depends import AirplaneServiceDep, check_admin_privileges

router = APIRouter(prefix='/airplanes',tags=['Airplane'])

@router.post('/')
def add_airplane(
    airplane_service:AirplaneServiceDep,
    airplane_details: AirplaneCreate = Depends(),
    admin: dict = Depends(check_admin_privileges)
    ):
    return airplane_service.create_airplane(airplane_details)

@router.get("/",response_model=list[AirplaneResponse])
def get_airplane(
    airplane_service: AirplaneServiceDep
): 
    return airplane_service.get_airplane_list()