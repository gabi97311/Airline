import jwt
from src.config_database.config import settings


def encode_jwt(
    payload: dict,
    private_key: str = settings.auth_jwt.private_key_file.read_text(),
    algorithm: str = settings.auth_jwt.algorithm,
):
    encoded = jwt.encode(payload, private_key, algorithm=algorithm)
    return encoded


def decode_jwt(
    token: str | bytes,
    public_key: str = settings.auth_jwt.public_key_file.read_text(),
    algorithm: str =settings.auth_jwt.algorithm,
):

    decode = jwt.decode(token, public_key, algorithms=[algorithm])
    return decode
