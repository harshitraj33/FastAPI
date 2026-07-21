from fastapi import APIRouter
from ..models.student import Student, Student_Response

student_router = APIRouter(
    prefix="/student",
    tags=["Students"] # Adding a tag for better OpenAPI docs organization
)
students=[]

@student_router.post("/", response_model=Student_Response, status_code=201)
def student_model(student : Student):
    students.append(student)
    return student
