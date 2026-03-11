from fastapi import APIRouter, Depends
from app.schemes.airplane_schemes import AirplaneCreate
from app.depends import AirplaneServiceDep, check_admin_privileges

router = APIRouter(prefix='/airplane',tags=['Airplane'])

@router.post('/')
def add_airplane(
    airplane_service:AirplaneServiceDep,
    airplane_details: AirplaneCreate = Depends(),
    admin: dict = Depends(check_admin_privileges)
    ):
    return airplane_service.create_airplane(airplane_details)