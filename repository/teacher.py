from sqlalchemy.orm import Session
from models.teacher import Teacher

def create_teacher(db: Session, teacher):
    db.add(teacher)
    db.commit()
    db.refresh(teacher)
    return teacher