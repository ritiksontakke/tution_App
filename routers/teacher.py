from fastapi import FastAPI
from fastapi import APIRouter
from schemas.teacher import CreateNewAccount, LoginTeacher

teacher_router = APIRouter()

@teacher_router.post("/create-new-account")
def createnewcccount(createAccount : CreateNewAccount):
    return ("create account succefully")

@teacher_router.post("/login")
def LoginAccount(login : LoginTeacher):
    return("login succefully")