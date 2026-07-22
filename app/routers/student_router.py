from fastapi import APIRouter, FastAPI
from ..models.student import Student, Student_Response, Student_Update
from app.services.student_service import add_student,get_all_student, get_one_student, update_student

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
    
@student_router.get("/get")
async def get_students():

    return await get_all_student()

#get student by id
@student_router.get("/getone", response_model=Student_Response)
async def get_only_one_student(id):
    return await get_one_student(id)

@student_router.put("/update", response_model=Student_Response)
async def updateStudent(id, student : Student_Update):
    return update_student(id,student)