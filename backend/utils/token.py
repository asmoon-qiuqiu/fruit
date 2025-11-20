# utils/token.py
import secrets
from datetime import datetime, timedelta
from config import RESET_TOKEN_EXPIRE_HOURS


def generate_reset_token() -> str:
    return secrets.token_urlsafe(32)


def get_reset_expiration() -> datetime:
    return datetime.now() + timedelta(hours=RESET_TOKEN_EXPIRE_HOURS)
