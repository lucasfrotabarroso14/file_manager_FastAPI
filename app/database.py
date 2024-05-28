from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#  URL de conexão com o banco de dados
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://docker:docker@localhost:3310/file_manager"

# função para retornar a SessionLocal
engine = create_engine(SQLALCHEMY_DATABASE_URL)

def get_session():
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()




Base = declarative_base()




from app.microservices.file_microservice.file_model import File
from app.microservices.organization_microservice.organization_model import Organization
from app.microservices.user_microservice.user_model import User