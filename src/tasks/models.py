from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from src.user.models import SharedUser

class Task(BaseModel):
    title : str
    description : str
    is_completed : bool = False
    creation_date: Optional[datetime] = None
    user : SharedUser
        
