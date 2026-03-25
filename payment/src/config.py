from pydantic_settings import BaseSettings 


class Settings(BaseSettings): 
    app_name: str = 'payment'
    debug: bool = True 
    DATABASE_URL: str
    
    cors_origins: list = [
        'http://localhost:3000',
        'http://127.0.0.1:3000'
    ]
    
    static_dir: str = 'static'
    class Config:
        env_file = '.env'
        extra = "ignore"
        
settings = Settings()