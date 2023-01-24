from .database import Base
from sqlalchemy import Column, String, Integer


class UsersDatabase(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    reps = Column(Integer)
