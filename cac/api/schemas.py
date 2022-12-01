from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic.types import conint

class EventBase(BaseModel):
    name: str
    description: str
    street: str
    city: str
    zip_code: str
    state: str
    event_timestamp: datetime

class PostBase(BaseModel):
    title: str
    content: str

class PostCreate(PostBase):
    pass

class UserOut(BaseModel):
    id: UUID
    email: EmailStr
    username: str
    created_at: datetime

    class Config:
        orm_mode = True

class Post(PostBase):
    id: UUID
    created_at: datetime
    owner_id: UUID
    owner: UserOut

    class Config:
        orm_mode = True

class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        orm_mode = True

class EventOut(EventBase):
    id: UUID
    created_at: datetime
    owner_id: UUID
    owner: UserOut

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[UUID] = None

class Vote(BaseModel):
    post_id: UUID
    dir: conint(le=1)