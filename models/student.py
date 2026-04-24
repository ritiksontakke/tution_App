from typing import List, Optional
from sqlalchemy import ForeignKey, String , Integer , Column
from sqlalchemy.orm import mapped_column, Mapped, relationship,DeclarativeBase
from db.database import Base
from sqlalchemy.orm import relationship

class Student(Base):
    __tablename__ = "student"
    
    id: Mapped[int] = mapped_column(primary_key=True)

    teacher_id: Mapped[int] = mapped_column(ForeignKey("teacher.id"))

    full_name: Mapped[str] = mapped_column(String(30))

    parent_no = Column(String(15), nullable=False)

    address: Mapped[str] = mapped_column(String(100))

    teacher_id = Column(Integer, ForeignKey("teacher.id"), nullable=False)
    teacher = relationship("Teacher", back_populates="students")