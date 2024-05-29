from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_session
from app.microservices.organization_microservice.organization_model import Organization
from app.microservices.organization_microservice.organization_schema import OrganizationSchema
from app.microservices.organization_microservice.organization_view import router
from app.microservices.user_microservice.user_repository import UserRepository
from app.microservices.user_microservice.user_schema import  UserSchema


async def get_all_users():
    try:
        user_service = UserRepository()
        all_users, status = user_service.get_all_users_db()
        if status:
            return {
                "status": True,
                "status_code": 200,
                "result": all_users,
            }
        else:
            return {
                "status": False,
                "status_code": 500,
                "result": "Error",
            }
    except Exception as e:
        return {
            "status": False,
            "status_code": 500,
            "result": str(e),
        }

@router.post("/user", response_model=OrganizationSchema)
async def create_user(user: UserSchema,db_session: Session = Depends(get_session)):
    try:
        user_repository = UserRepository(db_session)
        new_user, status = user_repository.create_new_user_db(name=user.name, email=user.email,password=user.password,organization_id=user.organization_id)
        if status:
            return new_user
        else:
            raise HTTPException(status_code=500, detail="Failed to create user")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))