from pydantic_settings import BaseSettings   ,SettingsConfigDict
 
class Settings(BaseSettings):
    PROJECT_NAME: str = "AI Powered Hospital Management System"
    VERSION: str = "1.0.0"

    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )
settings = Settings()