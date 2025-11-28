# 导入异步引擎和会话
from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel.ext.asyncio.session import AsyncSession
from config import DATABASE_URL

# 创建异步数据库引擎
# echo=True 用于调试，生产环境建议设为 False
async_engine = create_async_engine(DATABASE_URL, echo=True)


# 修改 get_session 为异步生成器
async def get_session():
    """异步获取数据库会话"""
    # 使用 AsyncSession 和 async with 来管理异步会话生命周期
    # 这里直接传入 engine，SQLModel/SQLAlchemy 会处理连接池等
    async with AsyncSession(async_engine) as session:
        try:
            # 将 session 对象提供给依赖它的函数
            yield session
        except Exception as e:
            # 记录或处理会话期间发生的错误
            # 注意：在异步上下文中，打印可能不是最佳的日志方式，
            # 考虑使用 logging 模块
            print(f"数据库会话错误：{e}")
            # 通常不需要手动关闭 session，async with 会处理
            # 抛出异常让 FastAPI 或调用者处理
            raise  # 重新抛出异常


# 注意：
# 1. 不再需要 from sqlmodel import create_engine, Session (除非还有其他地方用到同步 Session)
# 2. 不再需要手动 session.close()，async with 会自动处理
