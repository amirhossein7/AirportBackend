from typing import List
from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from database import get_db
from models import Company as CompanyModel
from schema import Company as CompanySchema


router = APIRouter()

@router.post("/create", response_model=CompanySchema)
async def createCompany(data: CompanySchema, db: Session = Depends(get_db)):
    query = CompanyModel(name=data.name)
    db.add(query)
    db.commit()
    db.refresh(query)
    msg = f"Company created"
    return {"message": msg, **query.__dict__}



@router.get("/getAll", response_model=List[CompanySchema], status_code=status.HTTP_200_OK)
async def getAllCompanies(db: Session = Depends(get_db)):
    query = db.query(CompanyModel).all()
    if query is None:
        return JSONResponse(content="There is no company!", status_code=status.HTTP_404_NOT_FOUND)
    else:
        return query
    

@router.get("/{id}", response_model=CompanySchema, status_code=status.HTTP_200_OK)
async def getCompany(id: int, db: Session = Depends(get_db)):
    query = db.query(CompanyModel).filter(CompanyModel.id == id).first()
    if query is None:
        return JSONResponse(content=f"Company not found wit id: {id}", status_code=status.HTTP_404_NOT_FOUND)
    else:
        return query
    
    
@router.delete("/delete/{id}", response_model=CompanySchema, status_code=status.HTTP_200_OK)
async def deleteCompany(id: int, db: Session = Depends(get_db)):
    query = db.query(CompanyModel).filter(CompanyModel.id == id).first()
    if query is None:
        return JSONResponse(content=f"Company not found with id: {id}", status_code=status.HTTP_404_NOT_FOUND)
    else:
        db.delete(query)
        db.commit()
        return JSONResponse(content=f"Company deleted with id: {id}", status_code=status.HTTP_200_OK)