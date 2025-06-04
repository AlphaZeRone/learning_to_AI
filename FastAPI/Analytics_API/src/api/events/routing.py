import os
from fastapi import APIRouter
from .schemas import (
    EventSchema, 
    EventListSchema, 
    EventCreateSchema,
    EventUpdateSchema
)

router = APIRouter()
from ..db.config import DATABASE_URL

# LIST VIEW
# GET /api/events
@router.get("/")
def read_events() -> EventListSchema:
    #list of events
    print(os.environ.get("DATABASE_URL", DATABASE_URL))
    return {
        "results": [
            {'id': 1}, {'id': 2}, {'id': 3}
        ],
        "count": 3
    }

@router.get("/{event_id}")
def get_event(event_id: int) -> EventSchema:
    # a single event
    return {"id": event_id}

# POST /api/events 
# CREATE DATA HERE
@router.post("/")
def create_event(payload:EventCreateSchema) -> EventSchema:
    # create a new event
    print(payload.page)
    data = payload.model_dump()
    return {"id": 123, **data}

# UPDATE this data
# PUT /api/events/{event_id}
@router.put("/{event_id}")
def update_event(event_id: int, payload:EventUpdateSchema = {}) -> EventSchema:
    print(payload.description)
    data = payload.model_dump()
    return {"id": event_id, **data}

# DELETE 

