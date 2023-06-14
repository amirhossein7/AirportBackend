from typing import List
from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from database import get_db
from models import User as UserModel
from schema import User as UserSchema

router = APIRouter()


@router.post("/create", response_model=UserSchema)
async def createUser(data: UserSchema, db: Session = Depends(get_db)):
    query = UserModel(name=data.name, surname=data.surname,
                       age=data.age, phone_number=data.phone_number, username=data.username,
                        password=data.password, email=data.email, gender=data.gender, address= data.address)
    db.add(query)
    db.commit()
    db.refresh(query)
    msg = f"User created"
    return {"message": msg, **query.__dict__}



@router.get("/getAll", response_model=List[UserSchema], status_code=status.HTTP_200_OK)
async def getAllUsers(db: Session = Depends(get_db)):
    query = db.query(UserModel).all()
    if query is None:
        return JSONResponse(content="There is no users!", status_code=status.HTTP_404_NOT_FOUND)
    else:
        return query
    

@router.get("/{id}", response_model=UserSchema, status_code=status.HTTP_200_OK)
async def getUser(id: int, db: Session = Depends(get_db)):
    query = db.query(UserModel).filter(UserModel.id == id).first()
    if query is None:
        return JSONResponse(content=f"User not found wit id: {id}", status_code=status.HTTP_404_NOT_FOUND)
    else:
        return query
        
        
@router.delete("/delete/{id}", response_model=UserSchema, status_code=status.HTTP_200_OK)
async def deleteCompany(id: int, db: Session = Depends(get_db)):
    query = db.query(UserModel).filter(UserModel.id == id).first()
    if query is None:
        return JSONResponse(content=f"User not found with id: {id}", status_code=status.HTTP_404_NOT_FOUND)
    else:
        db.delete(query)
        db.commit()
        return JSONResponse(content=f"User deleted with id: {id}", status_code=status.HTTP_200_OK)