from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.database import get_session
from app.microservices.organization_microservice.organization_repository import OrganizationRepository


router = APIRouter()
@router.get("/organizations")
async def get_all_organizations(DB_session : Session = Depends(get_session)):
    repository = OrganizationRepository(DB_session)
    organizations = repository.get_all_organizations()

    return organizations
