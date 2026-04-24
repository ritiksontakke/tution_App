from sqlalchemy.orm import Session
from models.student import Student
from schemas.student import CreateNewStudent, UpdateStudent

# 🔥 Repository imports
from repository.student import (
    create_student,
    get_student_by_id,
    get_all_students,
    update_student as repo_update_student,
    delete_student as repo_delete_student
)


# 🔥 CREATE
def create_new_student(db: Session, data: CreateNewStudent):

    student = Student(
        full_name=data.full_name,
        parent_no=data.parents_no,
        address=data.address,
        teacher_id=data.teacher_id
    )

    return create_student(db, student)


# 🔥 GET ONE
def get_student_service(db: Session, student_id: int):

    student = get_student_by_id(db, student_id)

    if not student:
        return {"error": "Student not found"}

    return student


# 🔥 GET ALL
def get_all_students_service(db: Session):

    return get_all_students(db)


# 🔥 UPDATE
def update_student_service(db: Session, student_id: int, data: UpdateStudent):

    student = get_student_by_id(db, student_id)

    if not student:
        return {"error": "Student not found"}

    if data.full_name is not None:
        student.full_name = data.full_name

    if data.parent_mob_no is not None:
        student.parent_mob_no = data.parent_mob_no

    if data.address is not None:
        student.address = data.address

    return repo_update_student(db, student)


# 🔥 DELETE
def delete_student_service(db: Session, student_id: int):

    student = get_student_by_id(db, student_id)

    if not student:
        return {"error": "Student not found"}

    return repo_delete_student(db, student)