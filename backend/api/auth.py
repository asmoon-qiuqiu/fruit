# api/auth.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import select, Session
from datetime import datetime

from model.user import User
from model.password_reset import PasswordReset
from schemas.auth import (
    UserRegister,
    UserLogin,
    PasswordResetRequest,
    PasswordResetConfirm,
    LoginResponse,
)
from schemas.user import UserResponse
from database import get_session
from utils.password import hash_password, verify_password
from utils.token import generate_reset_token, get_reset_expiration

router = APIRouter(prefix="/api/auth", tags=["auth"])


@router.post(
    "/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED
)
def register(user_data: UserRegister, session: Session = Depends(get_session)):
    statement = select(User).where(User.username == user_data.username)
    existing_user = session.exec(statement).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="用户名已被注册"
        )
    # 检查邮箱是否已存在
    statement = select(User).where(User.email == user_data.email)
    existing_email = session.exec(statement).first()
    if existing_email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="邮箱已被注册"
        )
    # 创建新用户
    new_user = User(
        username=user_data.username,
        email=user_data.email,
        hashed_password=hash_password(user_data.password),
    )

    session.add(new_user)
    session.commit()
    session.refresh(new_user)

    return new_user


@router.post("/login", response_model=LoginResponse)
def login(login_data: UserLogin, session: Session = Depends(get_session)):
    # ""用户登录""
    # 查找用户(支持用户名或邮箱登录)
    statement = select(User).where(
        (User.username == login_data.username) | (User.email == login_data.username)
    )
    user = session.exec(statement).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="用户名或密码错误"
        )

    if not verify_password(login_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="用户名或密码错误"
        )

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="账户已被禁用"
        )
    # 实际应用中应该生成JWT token
    token = f"mock_token_{user.id}_{secrets.token_urlsafe(16)}"

    return LoginResponse(
        message="登录成功",
        user=UserResponse(
            id=user.id,
            username=user.username,
            email=user.email,
            is_active=user.is_active,
            created_at=user.created_at,
        ),
        token=token,
    )


@router.post("/forgot-password")
def forgot_password(
    reset_request: PasswordResetRequest, session: Session = Depends(get_session)
):
    # 忘记密码 - 发送重置链接
    # 查找用户
    statement = select(User).where(User.email == reset_request.email)
    user = session.exec(statement).first()

    if not user:
        # 为了安全,即使用户不存在也返回成功消息
        return {"message": "如果该邮箱已注册,重置链接已发送到您的邮箱"}

    token = generate_reset_token()
    expires_at = get_reset_expiration()

    reset_record = PasswordReset(user_id=user.id, token=token, expires_at=expires_at)

    session.add(reset_record)
    session.commit()
    # 实际应用中这里应该发送邮件
    reset_link = f"http://localhost:5173/reset-password?token={token}"
    print(f"密码重置链接: {reset_link}")

    return {
        "message": "如果该邮箱已注册,重置链接已发送到您的邮箱",
        "debug_token": token,  # 仅用于测试,生产环境删除
    }


@router.post("/reset-password")
def reset_password(
    reset_data: PasswordResetConfirm, session: Session = Depends(get_session)
):
    """重置密码"""
    # 查找重置令牌
    statement = select(PasswordReset).where(
        PasswordReset.token == reset_data.token, PasswordReset.is_used == False
    )
    reset_record = session.exec(statement).first()

    if not reset_record:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="无效的重置令牌"
        )

    if datetime.now() > reset_record.expires_at:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="重置链接已过期"
        )
    # 更新用户密码
    statement = select(User).where(User.id == reset_record.user_id)
    user = session.exec(statement).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="用户不存在")

    user.hashed_password = hash_password(reset_data.new_password)
    user.updated_at = datetime.now()
    # 标记令牌为已使用
    reset_record.is_used = True

    session.add(user)
    session.add(reset_record)
    session.commit()

    return {"message": "密码重置成功"}


@router.get("/verify-reset-token/{token}")
def verify_reset_token(token: str, session: Session = Depends(get_session)):
    #  """验证重置令牌是否有效"""
    statement = select(PasswordReset).where(
        PasswordReset.token == token, PasswordReset.is_used == False
    )
    reset_record = session.exec(statement).first()

    if not reset_record or datetime.now() > reset_record.expires_at:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="无效或已过期的令牌"
        )

    return {"message": "令牌有效", "valid": True}
