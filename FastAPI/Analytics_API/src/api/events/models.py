from typing import Optional, List
from sqlmodel import Field, SQLModel, create_engine

class EventModel(SQLModel, table=True):
    id: Optional[int] = Field(default = None, primary_key=True)
    page: Optional[str] = ""
    description: Optional[str] = ""

class EventCreateSchema(SQLModel):
    page: str
    description: Optional[str] = ""

class EventUpdateSchema(SQLModel):
    page: Optional[str] = ""

class EventListSchema(SQLModel):
    results: List[EventModel]
    count: int


