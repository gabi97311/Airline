import Airline.auth.src.jwt as jwt
from fastapi import HTTPException
from datetime import datetime, timedelta
from Airline.auth.src.jwt import ExpiredSignatureError, InvalidTokenError

from app.core import settings

class JwtService:

    @staticmethod
    def encode_jwt(
        playload: dict,
        private_key: str = settings.auth_jwt.private_key_file.read_text(),
        algorithm: str = settings.auth_jwt.algorithm,
        expire_timedelta: timedelta | None = None,
        expire_minutes: int = settings.auth_jwt.access_token_expire_mins,
    ):
        to_encode = playload.copy()
        now = datetime.utcnow()

        if expire_timedelta:
            expire = now + expire_timedelta
        else:
            expire = now + timedelta(minutes=expire_minutes)

        to_encode.update(iat=now, exp=expire)

        encoded = jwt.encode(to_encode, private_key, algorithm=algorithm)
        return encoded

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
    def decode_analytics_token(analytics_token: str | bytes):
        try:
            analytics_public_key = settings.auth_jwt.analytics_public_key_file.read_text()
            return jwt.decode(
                analytics_token,
                key=analytics_public_key,
                algorithms=[settings.auth_jwt.algorithm],
            )
        except:
            raise HTTPException(status_code=401, detail=f"Invalid token.")
