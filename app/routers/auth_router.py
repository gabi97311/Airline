from fastapi import APIRouter, Form, Response
from app.schemes import RegisterSchemes
from app.depends import AuthServiceDep

router = APIRouter(prefix='/auth', tags=['Auth'])


@router.post('/register')
async def register_new_user(user: RegisterSchemes, auth_service: AuthServiceDep):
    return (await auth_service.register(
        user.user_name,
        user.user_password
    ))

@router.post('/login')
async def login(
    response: Response,
    auth_service: AuthServiceDep,
    user_name: str = Form(...),
    user_password: str = Form(...)
):
    try: 
        token_info = await auth_service.login(user_name, user_password)
    except Exception as e: 
        return e

    response.set_cookie(
        key="access_token",   
        value=token_info.access_token,
        httponly=True,
        secure=False,
        samesite="lax",
        max_age=3600
    )
    return {"message": "Sussesful, token has be save in cookies"}
    





