from pydantic_settings import BaseSettings
from pydantic import BaseModel
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

class AuthJWT(BaseModel):
    private_key_file: Path = BASE_DIR / 'certs' / 'jwt-private.pem'
    public_key_file: Path = BASE_DIR / 'certs' / 'jwt-public.pem'
    algorithm: str = 'RS256'
    access_token_expire_mins: int = 15

class Settings(BaseSettings):
    app_name: str = 'registration and authentication'
    debug: bool = True
    DATABASE_URL: str 
    cors_origins: list = [
        'http://localhost:3000',
        'http://127.0.0.1:3000'
    ]
    static_dir: str = 'static'
    
    auth_jwt: AuthJWT = AuthJWT()
    
    class Config:
        env_file = '.env'
        extra="ignore"
        
settings = Settings()
