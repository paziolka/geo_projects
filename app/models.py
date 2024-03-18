from .database import Base
from sqlalchemy import Column, Integer, String

class Projects(Base):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
