from typing import Annotated
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials\
    
from app.jwt import decode_jwt
from app.database import SessionDep
from app.services.auth_services import AuthServices
from app.services.user_services import UserServices
from app.services.flight_ticket_services import FlightTicketServices

from app.repositories.users_repositories import UsersRepositories
from app.repositories.flight_ticket_repositories import FlightTicketRepositories

http_bearer = HTTPBearer()

def get_current_token_payload(credentials: HTTPAuthorizationCredentials = Depends(http_bearer)):
    if not credentials:
        raise HTTPException(status_code=404,detail='token broken')
    token = credentials.credentials
    payload = decode_jwt(token=token)
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

def get_ticket_service(session: SessionDep) -> FlightTicketServices:
    return FlightTicketServices(FlightTicketRepositories(session))
    

AuthServiceDep = Annotated[AuthServices, Depends(get_auth_service)]
UserServiceDep = Annotated[UserServices, Depends(get_user_service)]
TicketServiceDep = Annotated[FlightTicketServices, Depends(get_ticket_service)]





