from fastapi import FastAPI
from routers.teacher import router

app = FastAPI()

app.include_router(router)

