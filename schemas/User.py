from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: str
    name: str
    surname: str
    age: int
    phone_number: str
    username: str
    password: str
    email: str
    gender: str
    address: Optional[str]