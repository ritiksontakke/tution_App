from sqlalchemy.orm import session
from models.student import Student
from schemas.student import CreateNewStudent, UpdateStudent, DeletStudent

def create_new_stuent(db : session , new_student : CreateNewStudent):
    student = Student(
        full_name = new_student.full_Name,
        parent_mob_no = new_student.Parents_No,
        address = new_student.address
    )
