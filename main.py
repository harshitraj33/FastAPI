from fastapi import FastAPI
from app.routers.student_router import student_router

app = FastAPI()
app.include_router(student_router)

import uvicorn
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
