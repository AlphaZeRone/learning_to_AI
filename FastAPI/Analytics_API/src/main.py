from contextlib import asynccontextmanager
from typing import Union

from fastapi import FastAPI
from api.events import router as event_router
from api.db.session import init_db

import time

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("⏳ Waiting for DB to boot fully...")
    time.sleep(5)
    init_db()
    yield


app =FastAPI(lifespan=lifespan)
app.include_router(event_router, prefix='/api/events')

# REST API



@app.get("/")
def read_root():
    return {"Hello": "Worlder"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return{"item_id": item_id, "q": q}

@app.get("/healthz")
def read_api_health():
    return {"status": "ok"}
