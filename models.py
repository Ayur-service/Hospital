from pydantic import BaseModel, validator
from typing import List, Optional


class BaseStaff(BaseModel):
    username: str
    password: str


class Staff(BaseStaff):
    hospital_id: str
    is_admin: bool
    access: List[str]

class Token(BaseModel):
    sub: str  # user_id or staff_id
    aud: str  # issued to whom (hospital or  user)
    expire: int


class StaffToken(Token):
    hospital_id: Optional[str]
    is_admin: bool = False
    access: List[str]
