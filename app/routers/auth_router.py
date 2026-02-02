from fastapi import APIRouter, Depends, Form

from app.database import SessionDep
from app.schemes import RegisterSchemes
from app.services import AuthServices
from app.repositories import UsersRepositories
from app.depends import AuthServiceDep

router = APIRouter(prefix='/auth', tags=['Auth'])


@router.post('/register')
def register_new_user(user: RegisterSchemes, auth_service: AuthServiceDep):
    return (auth_service.register(
        user.user_name,
        user.user_password
    ))

@router.post('/login')
def login(
    auth_service: AuthServiceDep,
    user_name: str = Form(...),
    user_password: str = Form(...)
):
    return auth_service.login(
        user_name,
        user_password
    )




