from sqlalchemy.orm import Session

from app.microservices.user_microservice.user_model import User


class UserRepository():
    def __init__(self, session : Session):
        self.db_session = session


    def get_all_users_db(self):
        try:
            all_users = (self.db_session.query(User).join(User.organization)
                         .with_entities(
                                User,
                                User.organization.name.label('organization_name'),
                    ).all()
            )
            return all_users

        except Exception as e:
            return str(e), False


    def create_new_user_db(self, name: str, email: str, password: str, organization_id : int):
        try:

            new_user = User(name=name, email=email, password=password, organization_id=organization_id)
            self.db_session.add(new_user)
            self.db_session.commit()
            return new_user.id, True

        except Exception as e:

            self.db_session.rollback()
            return str(e), False

