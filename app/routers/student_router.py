from fastapi import APIRouter, FastAPI
from ..models.student import Student, Student_Response
from app.services.student_service import add_student

student_router = FastAPI()
student_router = APIRouter(
    prefix="/student",
    tags=["Students"]
)

@student_router.post("/add")
async def student_model(student : Student):
    
    student_data = student.model_dump()
    student_id = await add_student(student_data)
    return {
        "message":"student added",
        "id" : str(student_id)
    }