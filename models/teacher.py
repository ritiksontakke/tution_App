from typing import List, Optional
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import mapped_column, Mapped, relationship,DeclarativeBase
from db.database import Base

class Teacher(Base):
    __tablename__ = "teacher"

    id: Mapped[int] = mapped_column(primary_key=True)
    full_name: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(50))   # ✅ fix
    password: Mapped[str] = mapped_column(String(255))