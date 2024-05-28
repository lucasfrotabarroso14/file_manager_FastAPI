from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.shared.config.base import Base


class Organization(Base):
    __tablename__ = 'Organizations'

    id = Column(Integer, primary_key = True, autoincrement = True)
    name = Column(String(100))
    users = relationship('User', back_populates = 'users')
