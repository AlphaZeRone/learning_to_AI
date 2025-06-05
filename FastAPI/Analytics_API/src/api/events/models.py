from typing import Optional, List
from sqlmodel import Field, SQLModel, create_engine
from datetime import datetime, timezone, timedelta
from zoneinfo import ZoneInfo
import sqlmodel

def get_utc_now():
    utc_plus_7 = timezone(timedelta(hours=7))
    return datetime.now(utc_plus_7).replace(tzinfo = utc_plus_7)

class EventModel(SQLModel, table=True):
    id: Optional[int] = Field(default = None, primary_key=True)
    page: Optional[str] = ""
    description: Optional[str] = ""
    created_at: datetime = Field(
        default_factory = get_utc_now,
        sa_type = sqlmodel.DateTime(timezone=True),
        nullable = False
    )
    updated_at: datetime = Field(
        default_factory = get_utc_now,
        sa_type = sqlmodel.DateTime(timezone=True),
        nullable = False
    )

class EventCreateSchema(SQLModel):
    page: str
    description: Optional[str] = ""

class EventUpdateSchema(SQLModel):
    description: Optional[str] = ""

class EventListSchema(SQLModel):
    results: List[EventModel]
    count: int


