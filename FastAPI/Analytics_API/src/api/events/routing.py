import os
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from api.db.session import get_session

from .models import (
    EventModel, 
    EventListSchema, 
    EventCreateSchema,
    EventUpdateSchema
)

router = APIRouter()
from ..db.config import DATABASE_URL

# LIST VIEW
# GET /api/events
@router.get("/", response_model=EventListSchema)
def read_events(session: Session = Depends(get_session)):

#sort query by id and up by id
    query = select(EventModel).order_by(EventModel.id.asc()).limit(10)
    results = session.exec(query).all()
    #list of events
    print(os.environ.get("DATABASE_URL", DATABASE_URL))
    return {
        "results": results,
        "count": len(results)
    }

@router.get("/{event_id}", response_model=EventModel)
def get_event(event_id: int, session: Session = Depends(get_session)):
    # a single event
    query = select(EventModel).where(EventModel.id == event_id)
    result = session.exec(query).first()
    if not result :
        raise HTTPException(status_code=404, detail="Event not found")
    return result

# POST /api/events 
# CREATE DATA HERE
@router.post("/", response_model=EventModel)
def create_event(
    payload:EventCreateSchema, 
    session: Session = Depends(get_session)):
    # create a new event
    print(payload.page)
    data = payload.model_dump()
    obj = EventModel.model_validate(data)
    session.add(obj)
    session.commit()
    session.refresh(obj)
    return obj

# UPDATE this data
# PUT /api/events/{event_id}
@router.put("/{event_id}", response_model=EventModel)
def update_event(event_id:int, payload:EventUpdateSchema, session:Session = Depends(get_session)):
    query = select(EventModel).where(EventModel.id == event_id)
    obj = session.exec(query).first()
    if not obj:
        raise HTTPException(status_code=404, detail="Event not found")
    
    data = payload.model_dump()
    for k, v in data.items():
        setattr(obj, k, v)
    session.add(obj)
    session.commit()
    session.refresh(obj)
    return obj

# DELETE 
@router.delete("/{event_id}", response_model=EventModel)
def delete_event(event_id: int, session:Session = Depends(get_session)):
    query = select(EventModel).where(EventModel.id == event_id)
    obj = session.exec(query).first()
    if not obj:
        raise HTTPException(status_code=404, detail="Event not found")
    session.delete(obj)
    session.commit()
    session.refresh(obj)
    return obj
