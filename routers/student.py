from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.dependency import get_db
from schemas.student import CreateNewStudent, UpdateStudent

# 🔥 Service imports
from services.student import (
    create_new_student,
    get_student_service,
    get_all_students_service,
    update_student_service,
    delete_student_service
)

student_router = APIRouter()


# 🔥 CREATE
@student_router.post("/students")
def create_student(data: CreateNewStudent, db: Session = Depends(get_db)):
    return create_new_student(db, data)


# 🔥 GET ALL
@student_router.get("/students")
def get_all_students(db: Session = Depends(get_db)):
    return get_all_students_service(db)


# 🔥 GET ONE
@student_router.get("/students/{student_id}")
def get_student(student_id: int, db: Session = Depends(get_db)):
    return get_student_service(db, student_id)


# 🔥 UPDATE
@student_router.put("/students/{student_id}")
def update_student(student_id: int, data: UpdateStudent, db: Session = Depends(get_db)):
    return update_student_service(db, student_id, data)


# 🔥 DELETE
@student_router.delete("/students/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    return delete_student_service(db, student_id)