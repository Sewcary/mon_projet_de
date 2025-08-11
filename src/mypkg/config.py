# Contenu initial de src/mypkg/config.py
from dataclasses import dataclass
from dotenv import load_dotenv
import os

@dataclass
class Config:
    env: str = "dev"
    data_path: str = "data/input.csv"
    log_level: str = "INFO"

    @classmethod
    def from_env(cls) -> "Config":
        load_dotenv()
        return cls(
            env=os.getenv("APP_ENV", "dev"),
            data_path=os.getenv("DATA_PATH", "data/input.csv"),
            log_level=os.getenv("LOG_LEVEL", "INFO"),
        )