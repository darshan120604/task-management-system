from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

#Task Create Model
class TaskCreate(BaseModel):
    title:str = Field(...,min_length=2,max_length=100)
    description:str | None = None
    assigned_user_id : str
    due_date: datetime | None

#Task Update Model
class TaskUpdate(BaseModel):
    status:str = Field(..., pattern="^(Pending|In Progress|Completed)$")

#Task Response Model
class TaskResponse(BaseModel):
    id:int
    title:str
    description:str | None = None
    assigned_user: str
    due_date: datetime | None = None
    create_date: datetime

    class Config:
        from_attributes=True
