from fastapi import FastAPI
from pydantic import BaseModel , EmailStr , Field
from typing import Annotated

class CreateStudent(BaseModel):
    full_Name : Annotated[str, Field(min_length=2 , max_length=20)]
    Parents_No : int
    address : str
    roll_number : str

class UpdateStudent(BaseModel):
    full_name : Annotated[str, Field(min_length=2, max_length=20)]
    Parent_No : int
    address : str
    roll_number : str

class DeletStudent(BaseModel):
    full_name : Annotated[str, Field(min_length=2, max_length=20)]
    roll_number : int