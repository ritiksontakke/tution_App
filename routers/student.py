from fastapi import FastAPI
from fastapi import APIRouter
from schemas.student import CreateNewStudent, UpdateStudent, DeletStudent

student_router = APIRouter()

@student_router.post("/create-new-student")
def create_new_students(data: CreateNewStudent):
    return data

@student_router.put("/student-data-update")
def update_student_data(data: UpdateStudent):
    return data

@student_router.delete("/delete-student-data")
def delete_student_data(data : DeletStudent):
    return data