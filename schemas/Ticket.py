from pydantic import BaseModel
# from typing import Optional


class Ticket(BaseModel):
    id: str
    flight_id: str
    user_id: str
    price: float
    sitNumber: int
    type: str