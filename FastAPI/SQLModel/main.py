from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import SQLModel, create_engine, Session, Field, select, Relationship
from typing import Optional


class Hero(SQLModel, table=True):
    id: Optional[int] = Field(primary_key = True, index = True)
    name: str
    secret_name: str
    age: Optional[int] = None

    team_id: Optional[int] = Field(default = None, foreign_key = "team.id")
    missions: list["Mission"] = Relationship(
        back_populates = "hero", link_model = "HeroMissionLink"
    )

class Team(SQLModel, table=True):
    id: Optional[int] = Field(primary_key = True, default = None)
    name: str

    heroes: list[Hero] = Relationship(back_populates = "team")
    
class Mission(SQLModel, table=True):
    id: Optional[int] = Field(primary_key = True, default = None)
    description: str

    heroes: list[Hero] = Relationship(
        back_populates = "missions", link_model = "HeroMissionLink"
    )

class HeroMissionLink(SQLModel, table=True):
    hero_id: int = Field(
        default = None, foreign_key = "hero.id", primary_key = True
    )

    mission_id: int = Field(
        default = None, foreign_key = "mission.id", primary_key = True
    )
    
app = FastAPI()

#database connection
DATABASE_URL = "sqlite:///database.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SQLModel.metadata.create_all(engine)

#dependency
def get_db():
    with Session(engine) as session:
        yield session

#create Hero
@app.post("/heroes/", response_model = Hero)

def create_hero(hero: Hero, db: Session = Depends(get_db)):
    db.add(hero)
    db.commit()
    db.refresh(hero)
    return hero

#get all heroes
@app.get("/heroes", response_model = list[Hero])

def get_heros(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)): 
    heroes = db.execute(select(Hero).offset(skip).Limit(limit).all())
    return heroes

#get Hero by ID
@app.get("/heroes/{hero_id}", response_model = Hero)

def get_hero(hero_id: int, db: Session = Depends(get_db)):
    hero = db.get(Hero, hero_id)
    if not hero:
        raise HTTPException(status_code = 404, detail = "Hero not found")
    return hero

#Update Hero
@app.put("/heroes/{hero_id}", response_model = Hero)

def update_hero(hero_id: int, hero_data: Hero, db: Session = Depends(get_db)):
    hero = db.get(Hero, hero_id)
    if not hero:
        raise HTTPException(status_code = 404, detail = "Hero not found")
    for key, value in hero_data.model_dump().items():
        setattr(hero, key, value)

    db.commit()
    db.refresh(hero)
    return hero

#Delete hero
@app.delete("/heroes/{hero_id}", response_model = Hero)

def delete_hero(hero_id: int, db: Session = Depends(get_db)):
    hero = db.get(Hero, hero_id)
    if not hero:
        raise HTTPException(status_code = 404, detail = "Hero not found")
    db.delete(hero)
    db.commit()
    return hero





