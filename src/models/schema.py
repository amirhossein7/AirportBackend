from pydantic import BaseModel
from typing import Optional

class Airplane(BaseModel):
    id: str
    name: str
    number_of_sit: int

class Airport(BaseModel):
    id: str
    name: str
    address: str
    rate: float

class Company(BaseModel):
    id: str
    description: str

class Ticket(BaseModel):
    id: str
    origin: str
    takeoff_date: str
    landing_date: str
    airplain_id: str
    class_type: str

class Ticket(BaseModel):
    id: str
    flight_id: str
    user_id: str
    price: float
    sitNumber: int
    type: str


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