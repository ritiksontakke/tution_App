from fastapi import APIRouter , Depends
from sqlalchemy.orm import Session
from schemas.teacher import CreateNewAccount, LoginTeacher
from db.dependency import get_db
from services.teacher import create_new_account , login_teacher

teacher_router = APIRouter()

@teacher_router.post("/create-new-account")
def createnewcccount(createAccount : CreateNewAccount , db : Session = Depends(get_db)):
    return create_new_account(db, createAccount)

@teacher_router.post("/login")
def LoginAccount(login : LoginTeacher, db :Session = Depends(get_db)):
    return login_teacher(db, login)