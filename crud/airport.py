from typing import List
from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from database import get_db
from models import Airport as AirportModel
from schema import Airport as AirportSchema


router = APIRouter()

@router.post("/create", response_model=AirportSchema)
async def createAirport(data: AirportSchema, db: Session = Depends(get_db)):
    query = AirportModel(name=data.name, address=data.address)
    db.add(query)
    db.commit()
    db.refresh(query)
    msg = f"Airport created"
    return {"message": msg, **query.__dict__}



@router.get("/getAll", response_model=List[AirportSchema], status_code=status.HTTP_200_OK)
async def getAllAirports(db: Session = Depends(get_db)):
    query = db.query(AirportModel).all()
    if query is None:
        return JSONResponse(content="There is no airport!", status_code=status.HTTP_404_NOT_FOUND)
    else:
        return query
    

@router.get("/{id}", response_model=AirportSchema, status_code=status.HTTP_200_OK)
async def getAirport(id: int, db: Session = Depends(get_db)):
    query = db.query(AirportModel).filter(AirportModel.id == id).first()
    if query is None:
        return JSONResponse(content=f"Airport not found wit id: {id}", status_code=status.HTTP_404_NOT_FOUND)
    else:
        return query
    
    
@router.delete("/delete/{id}", response_model=AirportSchema, status_code=status.HTTP_200_OK)
async def deleteAirport(id: int, db: Session = Depends(get_db)):
    query = db.query(AirportModel).filter(AirportModel.id == id).first()
    if query is None:
        return JSONResponse(content=f"Airport not found with id: {id}", status_code=status.HTTP_404_NOT_FOUND)
    else:
        db.delete(query)
        db.commit()
        return JSONResponse(content=f"Airport deleted with id: {id}", status_code=status.HTTP_200_OK)
