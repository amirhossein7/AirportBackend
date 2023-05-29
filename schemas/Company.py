from pydantic import BaseModel
# from typing import Optional


class Company(BaseModel):
    id: str
    description: str