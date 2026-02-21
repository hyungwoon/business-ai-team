"""
Business AI Team - Configuration
"""
import os
from pathlib import Path
from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    """Application settings"""

    # API Keys
    anthropic_api_key: str

    # Model Configuration
    # 복잡한 분석/전략 작업 (Research, Marketing, Legal 등)
    model_name: str = "claude-sonnet-4-5"
    # 단순 처리 작업 (Productivity, Writing 등) - 비용 약 60~70% 절감
    model_name_light: str = "claude-haiku-4-5-20251001"

    # Project paths
    project_root: Path = Path(__file__).parent.parent

    class Config:
        env_file = ".env"
        case_sensitive = False


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance"""
    return Settings()
