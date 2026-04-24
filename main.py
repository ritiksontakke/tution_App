from fastapi import FastAPI
from routers.teacher import teacher_router
from routers.student import student_router
from db.database import engine, Base
import models.teacher
import models.student

app = FastAPI()
print(Base.metadata.tables) 
app.include_router(teacher_router)

app.include_router(student_router)

Base.metadata.create_all(bind=engine)