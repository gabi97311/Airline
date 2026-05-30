from pydantic_settings import BaseSettings
from pydantic import BaseModel
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
current_file_path = Path(__file__).resolve()
root_path = current_file_path.parent.parent.parent.parent.parent
dotenv_path = root_path / ".env"

class AuthJWT(BaseModel):
    private_key_file: Path = BASE_DIR / 'certs' / 'jwt-private.pem'
    public_key_file: Path = BASE_DIR / 'certs' / 'jwt-public.pem' 
    algorithm: str = 'RS256'

class Settings(BaseSettings): 
    debug: bool = True 
    ANALYTICS_DATABASE_URL: str
    AUTH_DATABASE_URL: str
    PAY_DATABASE_URL: str
    static_dir: str = str(dotenv_path)
    
    RMQ_URL: str
    
    auth_jwt: AuthJWT = AuthJWT()
    
    class Config:
        env_file = '.env'
        extra = "ignore"

settings = Settings()