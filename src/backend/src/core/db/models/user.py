from datetime import date
from typing import Literal

from sqlalchemy.orm import mapped_column, Mapped
from ..connect_db import Base

roles = Literal[
    "Ученик",
    "Учитель",
    "Администрация",
    "Персонал" ,
    "Родитель"
]

class User(Base):
    __tablename__ = "user"

    role: Mapped[Literal[roles]] = mapped_column()
    first_name: Mapped[str] = mapped_column()
    last_name: Mapped[str] = mapped_column()
    date_of_birth: Mapped[date] = mapped_column()