# backend/app/config.py

# from pydantic import BaseSettings
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # DATABASE_URL: str = "postgresql://user:password@localhost/dbname"
    DATABASE_URL: str = "mysql+pymysql://newuser:password@localhost:3306/inventory_db"

    SECRET_KEY: str = "your-secret-key"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    EMAIL_FROM: str = "noreply@yourdomain.com"

    class Config:
        env_file = ".env"

settings = Settings()
