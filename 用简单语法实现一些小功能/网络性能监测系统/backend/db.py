from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# ⚠️ 把 user 和 password 换成你自己的
DATABASE_URL = "mysql+pymysql://root:123456@127.0.0.1:3306/net_monitor?charset=utf8mb4"

engine = create_engine(
    DATABASE_URL,
    echo=False,
    pool_pre_ping=True
)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()
