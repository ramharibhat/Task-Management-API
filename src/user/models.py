from pydantic import BaseModel, EmailStr

class User(BaseModel):
    name: str
    email: EmailStr
    password: str


class SharedUser(BaseModel):
    name: str
    email: EmailStr

    class Config():
        from_attributes = True
