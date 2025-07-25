"""hardstyle/settings.py -- Settings for the hardstyle project."""

from pydantic_settings import BaseSettings


class LoggerSettings(BaseSettings):
    """Logger settings for the hardstyle project."""
    
    console: bool = True
    file: bool = True
    structured_file: bool = True
    save_path: str = "logs/hardstyle"
    level: str = "INFO"
    format: str = (
        "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
        "<level>{level: <8}</level> | "
        "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | "
        "<level>{message}</level>"
    )
    rotation: str = "100 MB"
    compression: str = "gz"
    retention: str = "1 week"
    rich_tracebacks: bool = True
    diagnose: bool = True
    
    model_config = {
        "extra": "ignore",  # Ignore extra fields from env
    }


class Settings(BaseSettings):
    """Settings for the hardstyle project."""
    
    logger: LoggerSettings = LoggerSettings()
    
    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
        "extra": "ignore",  # Ignore extra fields from env
    }


settings = Settings()