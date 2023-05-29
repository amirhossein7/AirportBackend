from pydantic import BaseModel
# from typing import Optional


class Airport(BaseModel):
    id: str
    name: str
    address: str
    rate: float