import jwt
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError
from fastapi import HTTPException, Depends, status, Cookie

from app.core import settings

class Jwt:
    @staticmethod
    def decode_jwt(token: str | bytes):
        try:
            public_key = settings.auth_jwt.public_key_file.read_text()
            return jwt.decode(
                token,
                key=public_key,
                algorithms=[settings.auth_jwt.algorithm],
            )
        except ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="Token expired")
        except InvalidTokenError as e:
            raise HTTPException(status_code=401, detail=f"Invalid token.")
    

    @staticmethod
    def get_current_token_payload(access_token: str | None = Cookie(default=None)):

        if not access_token:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Token invalid"
            )

        payload = Jwt.decode_jwt(token=access_token)

        if not payload:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Token invalid"
            )
        return payload

    @staticmethod
    async def get_current_auth_user(payload: dict = Depends(get_current_token_payload)
    ):
        user_id: int = int(payload.get("sub"))
        return user_id

    @staticmethod
    def check_admin_privileges(payload: dict = Depends(get_current_token_payload)):
        role = payload.get("role")
        if role != "admin":
            raise HTTPException(
                status_code=403,
                detail="You do not have enough permissions to perform this action",
            )
        return payload