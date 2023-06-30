from typing import List
from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from database import get_db
from models import Flight as FlightModel
from schema import Flight as FlightSchema


router = APIRouter()

@router.post("/create", response_model=FlightSchema)
async def createFlight(data: FlightSchema, db: Session = Depends(get_db)):
    query = FlightModel(origin_airport_id=data.origin_airport_id, destination_airport_id=data.destination_airport_id, takeoff_date=data.takeoff_date,
                         landing_date=data.landing_date, airplane_id=data.airplane_id, class_type=data.class_type)
    db.add(query)
    db.commit()
    db.refresh(query)
    msg = f"Flight created"
    return {"message": msg, **query.__dict__}



@router.get("/getAll", response_model=List[FlightSchema], status_code=status.HTTP_200_OK)
async def getAllFlights(db: Session = Depends(get_db)):
    query = db.query(FlightModel).all()
    if query is None:
        return JSONResponse(content="There is no flight!", status_code=status.HTTP_404_NOT_FOUND)
    else:
        return query
    

@router.get("/{id}", response_model=FlightSchema, status_code=status.HTTP_200_OK)
async def getFlight(id: int, db: Session = Depends(get_db)):
    query = db.query(FlightModel).filter(FlightModel.id == id).first()
    if query is None:
        return JSONResponse(content=f"Flight not found wit id: {id}", status_code=status.HTTP_404_NOT_FOUND)
    else:
        return query
    
    
@router.put("/update/{id}", response_model=FlightSchema, status_code=status.HTTP_200_OK)
async def updateFlight(data: FlightSchema, id: int, db: Session = Depends(get_db)):
    query = db.query(FlightModel).filter(FlightModel.id == id)
    if query is None:
        return JSONResponse(content=f"Flight not found wit id: {id}", status_code=status.HTTP_404_NOT_FOUND)
    else:
        query.update({"company_id": data.company_id, "airplane_id": data.airplane_id,
                       "origin": data.origin, "destination": data.destination,
                        "takeoff_date": data.takeoff_date, "landing_date": data.landing_date,
                          "class_type": data.class_type })
        db.commit()
        msg = f"Flight updated"
        return {"message": msg, **data.dict()}
    
@router.delete("/delete/{id}", response_model=FlightSchema, status_code=status.HTTP_200_OK)
async def deleteFlight(id: int, db: Session = Depends(get_db)):
    query = db.query(FlightModel).filter(FlightModel.id == id).first()
    if query is None:
        return JSONResponse(content=f"Flight not found with id: {id}", status_code=status.HTTP_404_NOT_FOUND)
    else:
        db.delete(query)
        db.commit()
        return JSONResponse(content=f"Flight deleted with id: {id}", status_code=status.HTTP_200_OK)
