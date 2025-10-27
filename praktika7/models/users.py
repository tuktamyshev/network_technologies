from pydantic import BaseModel, EmailStr
from typing import List, Optional
from models.events import Event


class User(BaseModel):
    email: EmailStr
    password: str
    events: Optional[List[Event]] = []

    class Config:
        schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "password": "Strong!!!",
                "events": [],
            }
        }


class NewUser(User):
    pass


class UserSignIn(BaseModel):
    email: EmailStr
    password: str

    class Config:
        schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "password": "Strong!!!",
            }
        }
