from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime

from db import Base, engine


class NetworkMetric(Base):
    __tablename__ = "network_metrics"

    id = Column(Integer, primary_key=True, index=True)
    host = Column(String(50), nullable=False)
    latency_ms = Column(Float)
    packet_loss_percent = Column(Integer)
    http_response_ms = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    print("MySQL 表创建完成")
