from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def greet():
    return {"message": "Hello World"}

@app.get("/home")
def home():
    return "home Page"

@app.get("/about")
def about():
    return "about Page"

@app.get("/get")
async def async_api():
    return "Async API"

@app.post("/post")
def async_api():
    return "Post API"

@app.put("/put")
def async_api():
    return "Put API"

@app.delete("/delete")
def async_api():
    return "Delete API"

@app.get("/getdata")
def get_student_data():
    students=[
        {"name": "aman", "roll no":21,"dept":"cse"},
        {"name": "raj", "roll no":22,"dept":"cse"}
    ]
    return students

@app.get("/getdata/{id:int}")
def path_param(id):
    return f"student id: {id}"

#create student list with name
#if entered name is in list/data simply return it
#otherwise return message data not found
@app.get("/getdatabyname/{name}")
def get_student_data_by_name(name: str):
    students = [
        {"name": "aman", "roll no": 21, "dept": "cse"},
        {"name": "raj", "roll no": 22, "dept": "cse"},
        {"name": "harsh", "roll no": 23, "dept": "it"},
    ]
    for student in students:
        if student["name"].lower() == name.lower():
            return student
    return {"message": "Data not found"}

@app.get("/student")
def get_query(dept : str, cgpa : float):
    students = [
        {"name": "aman", "roll no": 21, "dept": "cse", "cgpa": 5.5},
        {"name": "raj", "roll no": 22, "dept": "cse", "cgpa": 6.5},
        {"name": "harsh", "roll no": 23, "dept": "it", "cgpa": 7.5},
    ]
    result = []
    for student in students:
        if student["dept"].lower() == dept.lower() and student["cgpa"] >= cgpa:
            result.append(student)
    return result



