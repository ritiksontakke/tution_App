from sqlalchemy.orm import Session
from models.student import Student


# 🔥 CREATE
def create_student(db: Session, student: Student):
    db.add(student)
    db.commit()
    db.refresh(student)
    return student


# 🔥 GET BY ID
def get_student_by_id(db: Session, student_id: int):
    return db.query(Student).filter(Student.id == student_id).first()


# 🔥 GET ALL
def get_all_students(db: Session):
    return db.query(Student).all()


# 🔥 UPDATE
def update_student(db: Session, student: Student):
    db.commit()
    db.refresh(student)
    return student


# 🔥 DELETE
def delete_student(db: Session, student: Student):
    db.delete(student)
    db.commit()
    return {"message": "Student deleted successfully"}