from pydantic import BaseModel
from typing import List, Optional

#Step 4: Create Pydantic models

#Base model
class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None
    owner_id: int

#Request model
class ItemCreate(ItemBase):
    pass

#Response model
class ItemResponse(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True 

class UserBase(BaseModel):
    id: int
    email: str
    firstname: str
    lastname: str

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    is_activated: bool
    items: List[ItemResponse] = []

    class Config:
        orm_mode = True
