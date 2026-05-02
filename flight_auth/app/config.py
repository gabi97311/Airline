from pydantic_settings import BaseSettings
from pydantic import BaseModel
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
current_file_path = Path(__file__).resolve()
root_path = current_file_path.parent.parent.parent

dotenv_path = root_path / ".env"

class AuthJWT(BaseModel):
    private_key_file: Path = BASE_DIR / 'certs' / 'jwt-private.pem'
    public_key_file: Path = BASE_DIR / 'certs' / 'jwt-public.pem'
    analytics_public_key_file: Path = BASE_DIR / 'certs' / 'jwt-analytics_public.pem'
    algorithm: str = 'RS256'
    access_token_expire_mins: int = 15


class Settings(BaseSettings):
    app_name: str = 'registration and authentication'
    debug: bool = True
    static_dir: str = 'static'
    AUTH_DATABASE_URL: str 
    auth_jwt: AuthJWT = AuthJWT()
    cors_origins: list = [
        'http://localhost:3000',
        'http://127.0.0.1:3000'
    ]
    
    #RabbitMQ
    RMQ_URL: str
    payment_queue: str
    
    class Config:
        env_file = str(dotenv_path)
        extra="ignore"
        
settings = Settings()
