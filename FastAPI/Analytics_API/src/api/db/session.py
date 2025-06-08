import time
import timescaledb
from sqlmodel import SQLModel, create_engine, Session
from .config import DATABASE_URL, DB_TIMEZONE
from sqlalchemy.exc import OperationalError

if DATABASE_URL == "":
    raise NotImplementedError("DATABASE_URL is not set")

engine = timescaledb.create_engine(DATABASE_URL, timezone = DB_TIMEZONE)

def init_db():
    retries = 10
    delay = 2

    for i in range(retries):
        try:
            print(f"🔁 Connecting to DB... Attempt {i+1}")
            with engine.connect() as conn:
                print("✅ DB connected")
                break
        except OperationalError as e:
            print(f"❌ DB connection failed:", e)
            if i < retries - 1: 
                time.sleep(delay)
            else:
                raise RuntimeError("could not connect to the database") from e
            
    SQLModel.metadata.create_all(engine)

    # ✅ ให้ TimescaleDB สร้าง model ที่สืบทอดจาก TimescaleModel
    try:
        timescaledb.metadata.create_all(engine)
    except Exception as e:
        print('⚠️ Warning: Timescale hypertable setup failed:', e)




def get_session():
    with Session(engine) as session:
        yield session