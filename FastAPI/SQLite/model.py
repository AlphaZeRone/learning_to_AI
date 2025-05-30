from .database import Base, engine
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

#Step 2: Create ORM Models
class UserDB(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key = True, index = True)
    email = Column(String, unique = True, index = True)
    password = Column(String)
    is_activated = Column(Boolean, default = True)
    firstname = Column(String, index = True)
    lastname = Column(String, index = True)

    items = relationship("ItemDB", back_populates = "owner")

class ItemDB(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key = True)
    title = Column(String, index = True)
    description = Column(String, index = True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("UserDB", back_populates = "items")

#Step 3: Create the database
Base.metadata.create_all(bind = engine)
