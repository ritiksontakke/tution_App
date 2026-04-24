from typing import List, Optional
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import mapped_column, Mapped, relationship,DeclarativeBase

class Base(DeclarativeBase):
    pass

class Student(Base):
    __tablename__ = "student"
    
    teacher_id : int
    full_name : Mapped[str] = mapped_column(String(30))
    parent_mob_no : int
    address : str