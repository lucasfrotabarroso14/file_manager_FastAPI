from sqlalchemy.orm import declarative_base


Base = declarative_base()


from app.modules.file_microservice.file_model import File
from app.modules.organization_microservice.organization_model import Organization
from app.modules.permission_microservice.permission_model import Permission
from app.modules.user_microservice.user_model import User