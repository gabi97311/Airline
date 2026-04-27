from pydantic_settings import BaseSettings 
from pydantic import BaseModel
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
current_file_path = Path(__file__).resolve()
root_path = current_file_path.parent.parent.parent.parent
dotenv_path = root_path / ".env"

class AuthJWT(BaseModel):
    public_key_file: Path = BASE_DIR / 'certs' / 'jwt-public.pem' 
    algorithm: str = 'RS256'

class Settings(BaseSettings): 
    app_name: str = 'payment'
    PAY_DATABASE_URL: str
    flight_auth_service: str
    
    STRIPE_SECRET_KEY: str
    STRIPE_WEBHOOK_SECRET: str
    
    RMQ_URL: str
    
    Payment_Status_Queue: str
    
    cors_origins: list = [
        'http://localhost:3000',
        'http://127.0.0.1:3000'
    ]
    
    auth_jwt: AuthJWT = AuthJWT()
    
    static_dir: str = 'static'
    debug: bool = True 
    class Config:
        env_file = str(dotenv_path)
        extra = "ignore"
        
settings = Settings()