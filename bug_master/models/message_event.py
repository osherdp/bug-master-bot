import datetime

from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship

from .base import BaseModule


class MessageEvent(BaseModule):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    job_id = Column(String, index=True, nullable=False)
    job_name = Column(String, index=True, nullable=False)
    url = Column(String, nullable=False)
    thread_ts = Column(Integer, index=True)
    time = Column(DateTime, default=datetime.datetime.now())
    channel_ts = Column(Float, index=True)

    channel_id = Column(String, ForeignKey("channels.id"), nullable=False)
    channel = relationship("Channel", foreign_keys=[channel_id])
