from src.database.core import Base
from datetime import datetime, timezone
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship


class TaskDB(Base):
    __tablename__ = "Tasks"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("Users.id"), nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    is_completed = Column(Boolean, nullable=False, default=False)
    creation_date = Column(DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))

    user = relationship("UserDB", back_populates="tasks")
