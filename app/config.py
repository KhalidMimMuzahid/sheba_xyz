# # Application Configuration
# from pydantic_settings import BaseSettings, SettingsConfigDict
# class Settings(BaseSettings):
#     DB_USER: str
#     DB_PASS: str
#     DB_NAME:str
#     SENDER_PASSWORD:str
#     JWT_SECRET: str
#     JWT_ALGORITHM: str
#     model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

# Config = Settings()


from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv
import os

# ✅ Force .env to load at runtime
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

class Settings(BaseSettings):
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    SENDER_PASSWORD: str
    JWT_SECRET: str
    JWT_ALGORITHM: str

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

Config = Settings()
