from typing import List, Optional

from fastapi import Form
from pydantic import BaseModel
    

class TodoItem(BaseModel):
    item: str

    class Config:
        schema_extra = {
            "example": {
            "item": "Read the next chapter of the book"
            }
        }

class TodoItems(BaseModel):
    todos: list[TodoItem]
    class Config:
        schema_extra = {
            "example": {
                "todos": [
                    {
                        "item": "Example schema 1!"
                    },
                    {
                        "item": "Example schema 2!",
                    }
                ]
            }
        }
        
class Todo(BaseModel):
    id: Optional[int] = None
    item: str

    @classmethod
    def as_form(cls, item: str = Form(...)):
        return cls(item=item)
