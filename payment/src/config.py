from pydantic_settings import BaseSettings 
from pydantic import BaseModel
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

class AuthJWT(BaseModel):
    public_key_file: Path = BASE_DIR / 'certs' / 'jwt-public.pem' 
    algorithm: str = 'RS256'

class Settings(BaseSettings): 
    app_name: str = 'payment'
    debug: bool = True 
    DATABASE_URL: str
    flight_auth_service: str
    STRIPE_SECRET_KEY: str
    STRIPE_WEBHOOK_SECRET: str
    
    cors_origins: list = [
        'http://localhost:3000',
        'http://127.0.0.1:3000'
    ]
    
    static_dir: str = 'static'
    
    auth_jwt: AuthJWT = AuthJWT()
    
    class Config:
        env_file = '.env'
        extra = "ignore"
        
settings = Settings()