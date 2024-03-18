#config.py
import os

class Settings:
    PROJECT_NAME:str = "Geo Projects 🗺️"
    PROJECT_VERSION: str = "1.0.0"
    DB_URL: str = os.getenv('DATABASE_URL')

settings = Settings()
