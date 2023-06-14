import uvicorn
from services import app
from router import router as main_router

app.openapi()
app.openapi_schema = False

app.include_router(main_router, prefix="/api/v1")

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=9001)
