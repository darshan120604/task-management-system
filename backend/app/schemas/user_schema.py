#Define user schema
from pydantic import BaseModel, EmailStr, Field
from datetime import datetime

#UserCreate Model
class UserCreate(BaseModel):
    name:str = Field(..., min_length=2, max_length= 100)
    email:EmailStr 
    password:str = Field(..., min_length=4)
    role:str = Field(..., pattern="^(Admin|Employee)$")

#UserLogin Model
class UserLogin(BaseModel):
    email:str
    password: str

#UserResponse Model
class UserResponse(BaseModel):
    id:str
    name:str
    email:str
    role:str
    created_at:datetime

    class Config:
        from_attributes = True
        