from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', extra='ignore')

    MONGO_DETAILS: str = "mongodb://127.0.0.1:27017"
    DATABASE_NAME: str = "fastapi_db"
    COLLECTION_NAME: str = "users"
