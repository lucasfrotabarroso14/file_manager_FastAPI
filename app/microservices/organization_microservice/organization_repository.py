
from sqlalchemy.orm import Session

from app.microservices.organization_microservice.organization_model import Organization
from app.microservices.user_microservice.user_model import User


class OrganizationRepository:
    def __init__(self, session : Session):
        self.DB_session = session

    def get_all_organizations(self):
        try:
            organizations = self.DB_session.query(Organization).all
        except Exception as e:
            return str(e), False
        return organizations, True


    def get_users_from_organization(self, organization_id):
        try:
            users =(
                self.DB_session.query(User)
                .filter(User.organization_id == organization_id)
                .all()
            )
            return users, True

        except Exception as e:
            return str(e), False



    def create_organization_db(self, organization_name):

        try:
            new_organization = Organization(name = organization_name)
            self.DB_session.add(new_organization)
            self.DB_session.commit()
            return new_organization, True

        except Exception as e:
            self.DB_session.rollback()
            return str(e), False







