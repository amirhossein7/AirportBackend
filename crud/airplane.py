from typing import List
from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from database import get_db
from models import Airplane as AirplaneModel
from schema import Airplane as AirplaneSchema


router = APIRouter()


@router.post("/create", response_model=AirplaneSchema)
async def createAirplane(data: AirplaneSchema, db: Session = Depends(get_db)):
    query = AirplaneModel(name=data.name, number_of_sit=data.number_of_sit)
    db.add(query)
    db.commit()
    db.refresh(query)
    msg = f"Apirplane created"
    return {"message": msg, **query.__dict__}


@router.get("/getAll", response_model=List[AirplaneSchema], status_code=status.HTTP_200_OK)
async def getAllAirplane(db: Session = Depends(get_db)):
    query = db.query(AirplaneModel).all()
    if query is None:
        return JSONResponse(content="There is no airplane!", status_code=status.HTTP_404_NOT_FOUND)
    else:
        return query
    
@router.put("/update/{id}", response_model=AirplaneSchema, status_code=status.HTTP_200_OK)
async def updateAirplane(data: AirplaneSchema, id: int, db: Session = Depends(get_db)):
    query = db.query(AirplaneModel).filter(AirplaneModel.id == id)
    if query is None:
        return JSONResponse(content=f"Airplane not found wit id: {id}", status_code=status.HTTP_404_NOT_FOUND)
    else:
        query.update({"name": data.name, "number_of_sit": data.number_of_sit})
        db.commit()
        msg = f"Apirplane updated"
        return {"message": msg, **data.dict()}
            

@router.get("/{id}", response_model=AirplaneSchema, status_code=status.HTTP_200_OK)
async def getAirplane(id: int, db: Session = Depends(get_db)):
    query = db.query(AirplaneModel).filter(AirplaneModel.id == id).first()
    if query is None:
        return JSONResponse(content=f"Airplane not found wit id: {id}", status_code=status.HTTP_404_NOT_FOUND)
    else:
        return query
    
    
@router.delete("/delete/{id}", response_model=AirplaneSchema, status_code=status.HTTP_200_OK)
async def deleteAirplane(id: int, db: Session = Depends(get_db)):
    query = db.query(AirplaneModel).filter(AirplaneModel.id == id).first()
    if query is None:
        return JSONResponse(content=f"Airplane not found with id: {id}", status_code=status.HTTP_404_NOT_FOUND)
    else:
        db.delete(query)
        db.commit()
        return JSONResponse(content=f"Airplane deleted with id: {id}", status_code=status.HTTP_200_OK)
