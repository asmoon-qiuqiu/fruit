# ==================== 密码重置模型 ====================
from sqlmodel import SQLModel, Field
from datetime import datetime


class PasswordReset(SQLModel, table=True):
    __tablename__ = "password_resets"

    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id", index=True)
    token: str = Field(unique=True, index=True, max_length=100)
    expires_at: datetime
    is_used: bool = Field(default=False)
    created_at: datetime = Field(default_factory=datetime.now)
