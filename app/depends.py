from typing import Annotated
from fastapi import Depends, HTTPException, Cookie, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
    
from app.jwt import decode_jwt
from app.database import SessionDep

from app.services.auth_services import AuthServices
from app.services.user_services import UserServices
from app.services.flight_services import FlightServices
from app.services.seat_services import SeatServices
from app.services.ticket_services import TicketServices
from app.services.airplane_service import AirplaneServices


from app.repositories.users_repositories import UsersRepositories
from app.repositories.flight_repositories import FlightRepositories
from app.repositories.seat_repositories import SeatRepositories
from app.repositories.ticket_repositories import TicketRepositories 
from app.repositories.airplane_repositories import AirplaneRepositories

http_bearer = HTTPBearer()

def get_current_token_payload(
    access_token: str | None = Cookie(default=None) 
):

    if not access_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail='Token invalid'
        )
    
    payload = decode_jwt(token=access_token)
    
    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Token invalid'
        )
        
    return payload

def get_current_auth_user(
    user_services: UserServiceDep,
    payload: dict = Depends(get_current_token_payload)):
    user_id: int = int(payload.get("sub"))
    user = user_services.get_user_info(user_id)
    return user


def check_admin_privileges(payload: dict = Depends(get_current_token_payload)):
    role = payload.get('role')
    if role != 'admin':
        raise HTTPException(status_code=403, detail="You do not have enough permissions to perform this action")
    return payload
    
def get_auth_service(session: SessionDep) -> AuthServices:
    return AuthServices(UsersRepositories(session))

def get_user_service(session: SessionDep) -> UserServices: 
    return UserServices(UsersRepositories(session))

def get_flight_service(session: SessionDep) -> FlightServices:
    return FlightServices(FlightRepositories(session))

def get_seat_service(session: SessionDep) -> SeatServices:
    return SeatServices(SeatRepositories(session))

def get_ticket_serivce(session: SessionDep) -> TicketServices:
    return TicketServices(TicketRepositories(session))
    
def get_airplane_service(session: SessionDep) -> AirplaneServices:
    return AirplaneServices(session,AirplaneRepositories(session))

AuthServiceDep = Annotated[AuthServices, Depends(get_auth_service)]
UserServiceDep = Annotated[UserServices, Depends(get_user_service)]
FlightServiceDep = Annotated[FlightServices, Depends(get_flight_service)]
SeatServiceDop = Annotated[SeatServices, Depends(get_seat_service)]
TicketServiceDep = Annotated[TicketServices, Depends(get_ticket_serivce)]
AirplaneServiceDep = Annotated[AirplaneServices,Depends(get_airplane_service)]




