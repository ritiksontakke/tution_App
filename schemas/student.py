from fastapi import FastAPI
from pydantic import BaseModel , EmailStr , Field
from typing import Annotated , Optional

class CreateNewStudent(BaseModel):
    full_Name : Annotated[str, Field(min_length=2 , max_length=20)]
    Parents_No : int
    address : str
    roll_number : str

class UpdateStudent(BaseModel):
    full_name : Optional[Annotated[str, Field(min_length=2, max_length=20 )]] = None
    Parent_No : Optional[str] = None
    address : Optional[str] = None
    roll_number : Optional[int] = None

class DeletStudent(BaseModel):
    full_name : Annotated[str, Field(min_length=2, max_length=20)]
    roll_number : int