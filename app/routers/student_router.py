from typing import List
from fastapi import FastAPI, APIRouter, Query
from app.models.student import Student, Student_Response, Student_Update

from app.services.student_service import add_student, delete_student, get_all_student, get_filterd_student_list, get_one_student, update_student


student_router = FastAPI()

student_router = APIRouter(
    prefix="/student"
)


@student_router.post("/add")
async def student_model(student : Student):

    student_data = student.model_dump()

    student_id = await add_student(student_data)

    return {
        "message":"Student added",
        "id" : str(student_id)
    }


@student_router.get("/get")
async def get_students():

    return await get_all_student()

#get student by id
@student_router.get("/getone", response_model=Student_Response)
async def get_only_one_student(id):
    return await get_one_student(id)

# update student router

@student_router.put("/update", response_model=Student_Update)
async def updateStudent(id, student : Student_Update):
    return await update_student(id, student)


@student_router.delete("/delete")
async def deleteStudent(id):
    await delete_student(id)
    return f"Student deleted : {id}"

@student_router.get("/filter")
async def get_filter_student(
    department : str = Query(None, description="filter by department name"),
    rollno: int = Query(None, description="filter by rollno"),
    min_cgpa : float = Query(None, description="min cgpa range"),
    max_cgpa : float = Query(None, description="max cgpa range"),
    name : str = Query(None, description="filter by name")
):
    
    if any([department,rollno,min_cgpa,max_cgpa,name]):

        return await get_filterd_student_list(
            department=department,
            rollno=rollno,
            min_cgpa=min_cgpa,
            max_cgpa=max_cgpa,
            name=name
        )
    
    else:
        return await get_all_student()