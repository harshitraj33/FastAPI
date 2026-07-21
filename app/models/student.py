from typing import Annotated
from pydantic import BaseModel, Field, EmailStr

class Student(BaseModel):
    name : str = Field(..., min_length=3, max_length=20)
    roll_no : int
    dept : str
    cgpa : float = Field(..., ge=4)
    email : EmailStr
    phone : Annotated[str, Field(pattern=r"[6-9]\d{10}$")]
    aadhar : str = Field(...,pattern=r"\d{12}$")
    pancard : str = Field(...,pattern=r"^[A-Z]{5}[0-9]{4}[A-Z]{1}$")
    password : str = Field(...,min_length=8)
    
    
class Student_Response(BaseModel):
    name : str
    roll_no : int
    dept : str
    cgpa : float
    email : EmailStr