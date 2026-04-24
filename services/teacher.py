from sqlalchemy.orm import Session
from models.teacher import Teacher
from schemas.teacher import  CreateNewAccount , LoginTeacher
from repository.teacher import create_teacher

def create_new_account(db: Session, data: CreateNewAccount):
    teacher = Teacher(
    full_name = data.full_name,
    email = data.email,
    password = data.password
    )
    return create_teacher(db , teacher)

def login_teacher(db : Session, login_data: LoginTeacher):
    teacher = db.query(Teacher).filter(
        Teacher.full_name == login_data.full_name
    ).first()

    if not teacher:
        return {"error" : "Teacher not found"}
    
    if teacher.password != login_data.password:
        return{"error" : "Invalid Password"}
    
    return{
        "message" : "Login Succesfully",
        "teacher.id" : "teacher.id",
        "name" : teacher.full_name
    }