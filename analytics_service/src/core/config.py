from pydantic_settings import BaseSettings 
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
current_file_path = Path(__file__).resolve()
root_path = current_file_path.parent.parent.parent.parent
dotenv_path = root_path / ".env"


class Settings(BaseSettings): 
    app_name: str = 'analytics'
    ANALYTICS_DATABASE_URL: str
    RMQ_URL: str
    
    cors_origins: list = [
        'http://localhost:3000',
        'http://127.0.0.1:3000'
    ]
    
    static_dir: str = 'static'
    debug: bool = True
    
     
    class Config:
        env_file = str(dotenv_path)
        extra = "ignore"
        
settings = Settings()