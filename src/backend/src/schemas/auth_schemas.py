from pydantic import BaseModel, Field
from typing import Literal
from datetime import date


roles = Literal[
    "Ученик",
    "Учитель",
    "Администрация",
    "Персонал" ,
    "Родитель"
]


class User(BaseModel):
    username: str = Field(max_length=255, min_length=5)
    password: str = Field(min_length=8, max_length=255)

class UserLogin(User):
    pass

class UserRegister(User):
    role: Literal[roles] = Field()
    first_name: str = Field()
    last_name: str = Field()
    date_of_birth: date = Field()