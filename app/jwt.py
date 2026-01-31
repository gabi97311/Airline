import jwt
from app.config import settings
from datetime import datetime, timedelta
from jwt import ExpiredSignatureError, InvalidTokenError
from fastapi import HTTPException


def encode_jwt(
    playload: dict, 
    private_key: str = settings.auth_jwt.private_key_file.read_text(),
    algorithm: str = settings.auth_jwt.algorithm,
    expire_timedelta: timedelta | None = None,
    expire_minutes: int = settings.auth_jwt.access_token_expire_mins
):
    to_encode = playload.copy()
    now = datetime.utcnow()
    
    if expire_timedelta:
        expire = now + expire_timedelta
    else: 
        expire = now + timedelta(minutes=expire_minutes)
    
    to_encode.update(
        iat = now,
        exp = expire
    )
    
    encoded = jwt.encode(to_encode, private_key, algorithm=algorithm)
    return encoded 

def decode_jwt(token: str | bytes):
    try:
        public_key = settings.auth_jwt.public_key_file.read_text()
        print(f"public_key: {public_key}")
        return jwt.decode(
            token,
            key=public_key,
            algorithms=[settings.auth_jwt.algorithm],
        )
    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except InvalidTokenError as e:
        raise HTTPException(status_code=401, detail=f"Invalid token. Reason: {e}")





