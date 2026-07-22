from app.core.collection import student_collection
async def add_student(student):
    result = await student_collection.insert_one(student)
    return result.inserted_id