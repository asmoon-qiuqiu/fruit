# schemas/auth.py
from pydantic import BaseModel, EmailStr, validator
from schemas.user import UserResponse
import re


class UserRegister(BaseModel):
    username: str
    email: EmailStr
    password: str

    @validator("username")
    def username_validator(cls, v):
        if len(v) < 3 or len(v) > 50:
            raise ValueError("用户名长度必须在3-50个字符之间")
        if not re.match(r"^[a-zA-Z0-9_\u4e00-\u9fa5]+$", v):
            raise ValueError("用户名只能包含字母、数字、下划线和中文")
        return v

    @validator("password")
    def password_validator(cls, v):
        if len(v) < 6:
            raise ValueError("密码长度至少6个字符")
        return v


class UserLogin(BaseModel):
    username: str
    password: str


class PasswordResetRequest(BaseModel):
    email: EmailStr


class PasswordResetConfirm(BaseModel):
    token: str
    new_password: str

    @validator("new_password")
    def password_validator(cls, v):
        if len(v) < 6:
            raise ValueError("密码长度至少6个字符")
        return v


class LoginResponse(BaseModel):
    message: str
    user: UserResponse
    token: str
