# settings.py
import os
from dotenv import load_dotenv
load_dotenv()

DATABASE_HOST = os.getenv("DATABASE_HOST")
DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
DATABASE_NAME = os.getenv("DATABASE_NAME")
DISCORD_CLIENT_TOKEN = os.getenv("DISCORD_CLIENT_TOKEN")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GOOGLE_CSE_KEY = os.getenv("GOOGLE_CSE_KEY")

