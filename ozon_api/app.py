from fastapi import FastAPI

from ozon_api.endpoints.endpoint import router as ozon_router

app = FastAPI()

app.include_router(ozon_router)
