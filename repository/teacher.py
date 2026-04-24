from sqlalchemy.orm import Session
from models.teacher import Teacher

def create_teacher(db: Session, teacher):
    db.add(teacher)
    db.commit()
    db.refresh(teacher)
    return teacher

def get_teacher_by_name(db : Session, full_name : str):
    return db.query(Teacher).filter(
        Teacher.full_name == full_name
    ).filter()