from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base


class Organization(Base):
    __tablename__ = 'Organizations'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))

    users = relationship("User", back_populates="organization")