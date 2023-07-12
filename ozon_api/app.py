from fastapi import FastAPI
from ozon_api.endpoint import router as ozon_router
from ozon_api.db.database import Base

app = FastAPI()

app.include_router(ozon_router)


@app.on_event("startup")
def startapp():
    Base.metadata.drop_all()
    Base.metadata.create_all()
