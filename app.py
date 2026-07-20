from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel, Field, EmailStr

app = FastAPI()

# Centralized student data
STUDENTS_DATA = [
    {"name": "aman", "roll_no": 21, "dept": "cse", "cgpa": 5.5},
    {"name": "raj", "roll_no": 22, "dept": "cse", "cgpa": 6.5},
    {"name": "harsh", "roll_no": 23, "dept": "it", "cgpa": 7.5},
]

@app.get("/")
def greet():
    return {"message": "Hello World"}

@app.get("/home")
def home_page():
    return "home Page"

@app.get("/about")
def about_page():
    return "about Page"

@app.get("/get")
def get_api():
    return "Async API"

@app.post("/post")
def post_api():
    return "Post API"

@app.put("/put")
def put_api():
    return "Put API"

@app.delete("/delete")
def delete_api():
    return "Delete API"

@app.get("/getdata")
def get_student_data():
    """Returns the complete list of student data."""
    return STUDENTS_DATA

@app.get("/getdata/{id:int}")
def get_student_by_id(id: int):
    """Returns a message with the student ID from the path."""
    return f"student id: {id}"

#create student list with name
#if entered name is in list/data simply return it
#otherwise return message data not found
@app.get("/getdatabyname/{name}")
def get_student_by_name(name: str):
    """Finds a student by name (case-insensitive) and returns their data."""
    for student in STUDENTS_DATA:
        if student["name"].lower() == name.lower():
            return student
    raise HTTPException(status_code=404, detail="Student not found")

@app.get("/student")
def get_students_by_query(dept : str, cgpa : float):
    """
    Filters students by department and a minimum CGPA.
    Example: /student?dept=cse&cgpa=6.0
    """
    filtered_students = [
        student for student in STUDENTS_DATA
        if student["dept"].lower() == dept.lower() and student["cgpa"] >= cgpa
    ]
    return filtered_students


class Student(BaseModel):
    name : str = Field(..., min_length=3, max_length=20)
    roll_no : int
    dept : str
    cgpa : float = Field(..., ge=4)
    email : EmailStr


students=[]

@app.post("/student/add")
def student_model(student : Student):
    students.append(student)
    
    return f"Student Added : {students}"










if __name__ == "__main__":
    # To run this file:
    # 1. Make sure you have uvicorn installed: pip install "uvicorn[standard]"
    # 2. Run the script: python app.py
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
