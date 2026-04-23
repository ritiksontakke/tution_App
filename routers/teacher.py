from fastapi import FastAPI
from fastapi import APIRouter
from schemas.teacher import CreateNewAccount, LoginTeacher

router = APIRouter()

@router.post("/create-new-account")
def createnewcccount(createAccount : CreateNewAccount):
    return {
        createAccount.full_name
    }

@router.post("/login")
def LoginAccount(login : LoginTeacher):
    return("login succefully")