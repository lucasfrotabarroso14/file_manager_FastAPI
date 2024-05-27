from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.shared.config.base import Base


class User(Base):
    __tablename__ = 'Permissions'

    id = Column(Integer, primary_key=True, autoincrement=True)
    file_id = Column(Integer, ForeignKey('Files.id'), nullable=False)
    permission_type= Column(Enum('Geral','Selecionados','Publico'), nullable=False,default='Geral')
    access_users_ids = Column(String,ForeignKey('Users.id'))
    uploader_user_id = Column(Integer,ForeignKey('Users.id'))

    file = relationship("File", back_populates="permissions")
    uploader = relationship("User", back_populates="uploaded_permissions")

