from typing import Optional

from pydantic import BaseModel



class UserBaseSchema(BaseModel):
    name: str
    email: str
    password: str
    organization_id: Optional[int]


class UserCreateSchema(UserBaseSchema):
    pass

class UserSchema(UserBaseSchema):
    id : int

    class Config:
        orm_mode = True