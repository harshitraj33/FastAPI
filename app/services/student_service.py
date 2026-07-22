from app.core.collection import student_collection
async def add_student(student):
    result = await student_collection.insert_one(student)
    return result.inserted_id

async def get_all_student():
    
    students_list = []

    async for student in student_collection.find():

        #type cast id into string
        student["_id"] = str(student["_id"])

        students_list.append(student)

    return students_list

from bson import ObjectId

async def get_one_student(id):

    #getting id from mongodb
    # in mongo id is stored as objectID
    student = await student_collection.find_one(
        {
            "_id" : ObjectId(id)
        }
    )

    if student:
        # convert object id into string
        student["_id"] = str(student["_id"])

    #create respective router 
    #return response body student_response
    return student

async def update_student(id,student_update):
    await student_collection.update_one(
        {
            "_id": ObjectId(id)
        },
        {
            "$set": student_update
        }
    )
    return student_update


async def delete_student(id):
    await student_collection.delete_one(
        {
            "_id" : ObjectId(id)
        }
    )