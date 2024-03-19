from .database import Base
from sqlalchemy import Column, Integer, String, JSON, Date

class Projects(Base):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    area_of_interest = Column(JSON)
    start_date = Column(Date)
    end_date = Column(Date)
