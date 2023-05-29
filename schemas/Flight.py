from pydantic import BaseModel
# from typing import Optional


class Ticket(BaseModel):
    id: str
    origin: str
    takeoff_date: str
    landing_date: str
    airplain_id: str
    class_type: str