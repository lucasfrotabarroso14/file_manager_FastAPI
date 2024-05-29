from urllib import request

from fastapi import APIRouter, HTTPException, Depends, Body
from sqlalchemy.orm import Session

from app.database import get_session
from app.microservices.organization_microservice.organization_repository import OrganizationRepository
from app.microservices.organization_microservice.organization_schema import OrganizationSchema, OrganizationCreateSchema

router = APIRouter()
@router.get("/organizations")
async def get_all_organizations(DB_session : Session = Depends(get_session)):
    repository = OrganizationRepository(DB_session)
    try:
        organizations, status = repository.get_all_organizations()

        if status:

            return {
                "status": True,
                "status_code": 200,
                "result": organizations,
            }
        else:
            return {
                "status": False,
                "status_code": 500,
                "result": 'failed to get organizations',

            }


    except Exception as e:

        return {
            "status": False,
            "status_code": 500,
            "result": str(e),

        }
@router.post("/organizations", response_model=OrganizationSchema)
async def create_new_organization(organization : OrganizationCreateSchema, DB_session: Session = Depends(get_session)):
    try:
        repository = OrganizationRepository(DB_session)
        new_organization, status = repository.create_organization_db(organization.name)

        if status:
            return new_organization
        else:
            raise HTTPException(status_code=500, detail="Failed to create organization")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))







