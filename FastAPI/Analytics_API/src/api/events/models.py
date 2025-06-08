from typing import Optional, List
from sqlmodel import Field, SQLModel
from datetime import datetime, timezone, timedelta
from timescaledb import TimescaleModel
import sqlmodel
from timescaledb.utils import get_utc_now


class EventModel(TimescaleModel, table=True):
    page: str = Field(index = True)
    description: Optional[str] = ""
    #created_at: datetime = Field(
        #default_factory = get_utc_now,
        #sa_type = sqlmodel.DateTime(timezone=True),
        #nullable = False
    #)

    updated_at: datetime = Field(
        default_factory = get_utc_now,
        sa_type = sqlmodel.DateTime(timezone=True),
        nullable = False
    )

    __chunk_time_interval__ = "INTERVAL 1 day"
    __drop_after__ = "INTERVAL 1 month"

class EventCreateSchema(TimescaleModel):
    page: str
    description: Optional[str] = ""

class EventUpdateSchema(TimescaleModel):
    description: Optional[str] = ""

class EventListSchema(TimescaleModel):
    results: List[EventModel]
    count: int

class EventBucketSchema(TimescaleModel):
    bucket: datetime
    page: str = Field(index=True)
    count: int
