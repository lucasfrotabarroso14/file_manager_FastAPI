from pydantic import BaseModel
from typing import Optional

class OrganizationBase(BaseModel):
    name: str

class OrganizationCreate(OrganizationBase):
    pass

class OrganizationSchema(OrganizationBase):
    id: int

    class Config:
        orm_mode = True