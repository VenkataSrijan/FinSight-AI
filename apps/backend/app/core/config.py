from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = Field(default="FinSight AI Backend")
    app_env: str = Field(default="development")
    app_debug: bool = Field(default=True)
    app_port: int = Field(default=8000)

    database_url: str
    redis_url: str

    secret_key: str
    jwt_access_expire_minutes: int = 15
    jwt_refresh_expire_days: int = 7

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()