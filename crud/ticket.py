from typing import List
from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from database import get_db
from models import Ticket as TicketModel
from schema import Ticket as TicketSchema


router = APIRouter()

@router.post("/create", response_model=TicketSchema)
async def createTicket(data: TicketSchema, db: Session = Depends(get_db)):
    query = TicketModel(flight_id=data.flight_id, user_id=data.user_id, price=data.price, sitNumber=data.sitNumber, type=data.type)
    db.add(query)
    db.commit()
    db.refresh(query)
    msg = f"Ticket created"
    return {"message": msg, **query.__dict__}



@router.get("/getAll", response_model=List[TicketSchema], status_code=status.HTTP_200_OK)
async def getAllTickets(db: Session = Depends(get_db)):
    query = db.query(TicketModel).all()
    if query is None:
        return JSONResponse(content="There is no ticket!", status_code=status.HTTP_404_NOT_FOUND)
    else:
        return query
    

@router.get("/{id}", response_model=TicketSchema, status_code=status.HTTP_200_OK)
async def getTicket(id: int, db: Session = Depends(get_db)):
    query = db.query(TicketModel).filter(TicketModel.id == id).first()
    if query is None:
        return JSONResponse(content=f"Ticket not found wit id: {id}", status_code=status.HTTP_404_NOT_FOUND)
    else:
        return query

@router.put("/update/{id}", response_model=TicketSchema, status_code=status.HTTP_200_OK)
async def updateTicket(data: TicketSchema, id: int, db: Session = Depends(get_db)):
    query = db.query(TicketModel).filter(TicketModel.id == id)
    if query is None:
        return JSONResponse(content=f"Ticket not found wit id: {id}", status_code=status.HTTP_404_NOT_FOUND)
    else:
        query.update({"flight_id": data.flight_id, "user_id": data.user_id,
                       "price": data.price, "sitNumber": data.sitNumber,
                        "type": data.type })
        db.commit()
        msg = f"Ticket updated"
        return {"message": msg, **data.dict()}
    
@router.delete("/delete/{id}", response_model=TicketSchema, status_code=status.HTTP_200_OK)
async def deleteTicket(id: int, db: Session = Depends(get_db)):
    query = db.query(TicketModel).filter(TicketModel.id == id).first()
    if query is None:
        return JSONResponse(content=f"Ticket not found with id: {id}", status_code=status.HTTP_404_NOT_FOUND)
    else:
        db.delete(query)
        db.commit()
        return JSONResponse(content=f"Ticket deleted with id: {id}", status_code=status.HTTP_200_OK)
