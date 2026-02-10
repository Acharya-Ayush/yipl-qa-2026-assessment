# utils/config.py
from dotenv import load_dotenv
import os

load_dotenv()  # load variables from .env
NAME = os.getenv("NAME")     
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
BASE_URL = os.getenv("BASE_URL")

