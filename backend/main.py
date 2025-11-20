# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager  # 导入生命周期装饰器
from sqlmodel import SQLModel
from api.auth import router as auth_router
from database import engine


app = FastAPI(title="水果商城用户认证API")

# CORS 配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# 创建表
# 1. 定义生命周期函数：启动时创建数据库表
@asynccontextmanager
async def lifespan(app: FastAPI):
    # 启动时执行的逻辑（替代原startup事件）
    SQLModel.metadata.create_all(engine)
    yield  # 应用运行中，此处可写关闭时的逻辑（如清理资源）


# 挂载路由
app.include_router(auth_router)


# 根路径
@app.get("/")
def root():
    return {
        "message": "水果商城用户认证API",
        "version": "1.0.0",
        "endpoints": {
            "register": "/api/auth/register",
            "login": "/api/auth/login",
            "forgot_password": "/api/auth/forgot-password",
            "reset_password": "/api/auth/reset-password",
        },
    }


# 启动命令（可选）
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
