from pydantic import BaseModel
from typing import Optional

class FileBase(BaseModel):
    file_name: str
    file_size: int
    file_type: str
    user_id: int

class FileCreate(FileBase):
    pass

class File(FileBase):
    id: int

    class Config:
        orm_mode = True