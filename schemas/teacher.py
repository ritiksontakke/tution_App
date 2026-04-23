from fastapi import FastAPI
from pydantic import BaseModel , Field , EmailStr
from typing import Annotated

class CreateNewAccount(BaseModel):
    full_name : Annotated[str,Field(min_length=2, max_length=20)]
    email : str
    password : str

class LoginTeacher(BaseModel):
    full_name : Annotated[str, Field(min_length=2 , max_length=20)]
    password : str