from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_session
from app.microservices.organization_microservice.organization_model import Organization
from app.microservices.organization_microservice.organization_schema import OrganizationSchema
from app.microservices.organization_microservice.organization_view import router
from app.microservices.user_microservice.user_repository import UserRepository
from app.microservices.user_microservice.user_schema import UserSchema, UserCreateSchema

routerteste = APIRouter()

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

@routerteste.post("/user", response_model=OrganizationSchema)
async def create_new_user(user_data: UserCreateSchema, db: Session = Depends(get_session)):
    try:
        repository = UserRepository(db)
        user_id, status = repository.create_new_user_db(
            name=user_data.name,
            email=user_data.email,
            password=user_data.password,
            organization_id=user_data.organization_id
        )

        if status:
            return {"id": user_id, "status": True, "status_code": 201}
        else:
            raise HTTPException(status_code=500, detail="Failed to create user")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))