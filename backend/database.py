from sqlmodel import create_engine, Session
from config import DATABASE_URL

# 数据库引擎
engine = create_engine(DATABASE_URL, echo=True)


def get_session():
    """获取数据库会话"""
    try:
        with Session(engine) as session:
            yield session
    except Exception as e:
        print(f"数据库会话错误：{e}")
