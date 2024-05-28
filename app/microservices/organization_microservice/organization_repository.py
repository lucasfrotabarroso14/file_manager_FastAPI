
from sqlalchemy.orm import Session

from app.microservices.organization_microservice.organization_model import Organization


class OrganizationRepository:
    def __init__(self, session : Session):
        self.DB_session = session

    def get_all_organizations(self):
        return self.DB_session.query(Organization).all




