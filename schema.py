from pydantic import BaseModel
from typing import Optional, List

class CustomBaseModel(BaseModel):
    class Config:
        orm_mode = True

class Airport(CustomBaseModel):
    id: Optional[int]
    name: str
    address: str

class Company(CustomBaseModel):
    id: Optional[int]
    name: str

class Flight(CustomBaseModel):
    id: Optional[int]
    airplane_id: int
    origin_airport_id: int
    destination_airport_id: int
    takeoff_date: str
    landing_date: str
    class_type: str

class Ticket(CustomBaseModel):
    id: Optional[int]
    flight_id: int
    user_id: int
    price: float
    sitNumber: int
    type: str


class User(CustomBaseModel):
    id: Optional[int]
    name: str
    surname: str
    age: int
    phone_number: str
    username: str
    password: str
    email: str
    gender: str
    address: Optional[str]

    tickets: List[Ticket] = []


class Airplane(CustomBaseModel):
    id: Optional[int]
    name: str
    number_of_sit: int

    flights: List[Flight] = []