from sqlmodel import create_engine, Session
from config import DATABASE_URL

# 数据库引擎
engine = create_engine(DATABASE_URL, echo=True)


def get_session():
    """获取数据库会话"""
    with Session(engine) as session:
        yield session
