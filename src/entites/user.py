from src.database.core import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class UserDB(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)

    #tasks = relationship("TaskDB", back_populates="user")