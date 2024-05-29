from pydantic import BaseModel
from typing import Optional

class OrganizationBaseSchema(BaseModel):
    name: str

class OrganizationCreateSchema(OrganizationBaseSchema):
    pass

class OrganizationSchema(OrganizationBaseSchema):
    id: int

    class Config:
        orm_mode = True