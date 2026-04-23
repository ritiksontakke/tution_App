from fastapi import FastAPI
from routers.teacher import teacher_router
from routers.student import student_router

app = FastAPI()

app.include_router(teacher_router)

app.include_router(student_router)