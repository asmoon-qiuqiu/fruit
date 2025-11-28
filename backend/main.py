# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager  # 导入生命周期装饰器
from sqlmodel import SQLModel
from api.auth import router as auth_router
from api.register import router as register
from database import async_engine


# 创建表
# 1. 定义生命周期函数：启动时创建数据库表
@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        # 启动逻辑
        async with async_engine.begin() as conn:
            await conn.run_sync(SQLModel.metadata.create_all)
        print("应用启动成功，数据库表已创建")
    except Exception as e:
        print(f"应用启动失败：创建数据库表出错 - {str(e)}")
        raise  # 重新抛出异常，终止应用启动

    yield

    try:
        # 关闭逻辑
        print("应用正在关闭...")
        await async_engine.dispose()
        print("应用已关闭，资源已清理")
    except Exception as e:
        print(f"应用关闭失败：清理资源出错 - {str(e)}")


app = FastAPI(title="水果商城用户认证API", lifespan=lifespan)

# CORS 配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 挂载路由
app.include_router(auth_router)
app.include_router(register)


# 根路径
@app.get("/")
def root():
    return {
        "message": "水果商城用户认证API",
        "version": "1.0.0",
        "endpoints": {
            "register": "/api/register",
            "login": "/api/auth/login",
            "forgot_password": "/api/auth/forgot-password",
            "reset_password": "/api/auth/reset-password",
        },
    }


# 启动命令（可选）
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
