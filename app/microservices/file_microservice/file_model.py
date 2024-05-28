from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class File(Base):
    __tablename__ = 'Files'

    id = Column(Integer, primary_key=True, index=True)
    file_name = Column(String(255))
    file_size = Column(Integer)
    file_type = Column(String(50))
    user_id = Column(Integer, ForeignKey('Users.id'))

    owner = relationship("User", back_populates="files")

