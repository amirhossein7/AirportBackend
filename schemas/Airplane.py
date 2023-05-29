from pydantic import BaseModel
# from typing import Optional

class Airplane(BaseModel):
    id: str
    name: str
    number_of_sit: int