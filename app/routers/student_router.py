from fastapi import FastAPI, APIRouter
from typing import List
from ..models.student import Student, Student_Response

student_router = FastAPI()
student_router = APIRouter(
    prefix="/student",
)
students=[]

@student_router.post("/add", response_model=List[Student_Response])
def student_model(student : Student):
    students.append(student)
    return students

@student_router.get("/student/get",response_model=Student_Response)
def getStudentDetails():
    student_detail = {"name":"amit", "rollno":21, "dept":"CSE", "cgpa":7, "email":"amit@gmail.com"}
    return student_detail
    
