from typing import Optional, List
from sqlmodel import Field, SQLModel, create_engine

class Event(SQLModel):
    id: int
    page: Optional[str] = ""
    description: Optional[str] = ""

