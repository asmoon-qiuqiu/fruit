import jwt
from datetime import datetime, timedelta
from config import RESET_TOKEN_EXPIRE_HOURS, SECRET_KEY, ALGORITHM


# 生成JWT Token
def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(datetime.UTC) + expires_delta
    else:
        expire = datetime.now(datetime.UTC) + timedelta(hours=RESET_TOKEN_EXPIRE_HOURS)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_reset_expiration() -> datetime:
    return datetime.now() + timedelta(hours=RESET_TOKEN_EXPIRE_HOURS)
