from pydantic import BaseModel
from typing import Optional
from models.Role import Role

class User(BaseModel):
    id:Optional[int]
    username: Optional[str]
    first_name:Optional[str]
    last_name:Optional[str]
    email:Optional[str]
    role:Optional[Role]
