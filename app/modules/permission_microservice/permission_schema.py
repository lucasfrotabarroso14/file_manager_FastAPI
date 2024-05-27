from pydantic import BaseModel
from typing import Optional

class PermissionBase(BaseModel):
    file_id: int
    permission_type: str
    access_users_ids: Optional[str]
    uploader_user_id: Optional[int]

class PermissionCreate(PermissionBase):
    pass

class Permission(PermissionBase):
    id: int

    class Config:
        orm_mode = True
