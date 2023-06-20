from typing import Optional

from pydantic import BaseSettings, PostgresDsn


class Settings(BaseSettings):
    DATABASE_URL: Optional[PostgresDsn] = None

    class Config:
        case_sensitive = True
        env_file = '.env'


settings = Settings()
