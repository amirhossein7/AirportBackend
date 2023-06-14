from fastapi import APIRouter
from crud.user import router as user_router
from crud.airplane import router as airplane_router
from crud.company import router as company_router
from crud.airport import router as airport_router
from crud.flight import router as flight_router
from crud.ticket import router as ticket_router

router = APIRouter()

router.include_router(user_router, prefix="/user", tags=["User"])
router.include_router(airplane_router, prefix="/airplane", tags=["Airplane"])
router.include_router(company_router, prefix="/company", tags=["Company"])
router.include_router(airport_router, prefix="/airport", tags=["Airport"])
router.include_router(flight_router, prefix="/flight", tags=["Flight"])
router.include_router(ticket_router, prefix="/ticket", tags=["Ticket"])


