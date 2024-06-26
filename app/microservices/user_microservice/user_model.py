from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class User(Base):
    __tablename__ = 'Users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    email = Column(String(100))
    password = Column(String(255))
    organization_id = Column(Integer, ForeignKey('Organizations.id'))

    organization = relationship("Organization", back_populates="users")
    files = relationship("File", back_populates="owner")