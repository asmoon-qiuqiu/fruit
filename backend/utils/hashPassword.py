from passlib.context import CryptContext

# 配置密码上下文，指定使用bcrypt算法
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    """
    对明文密码进行bcrypt哈希加密
    :param password: 用户输入的明文密码
    :return: 加密后的哈希字符串
    """
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    验证明文密码与哈希密码是否匹配
    :param plain_password: 用户输入的明文密码
    :param hashed_password: 数据库中存储的哈希密码
    :return: 匹配返回True，否则返回False
    """
    return pwd_context.verify(plain_password, hashed_password)
