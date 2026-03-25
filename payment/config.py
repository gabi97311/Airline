from pydantic_settings import BaseSettings 

class Settings(BaseSettings): 
    app_name: str = 'PAYMENT'
    debug: bool = True 
    DATABASE_URL: str
    
    class Config:
        env_file = '.env'
        
settings = Settings()