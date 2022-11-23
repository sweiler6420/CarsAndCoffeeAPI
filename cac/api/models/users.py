from pydantic import BaseModel
from sqlalchemy.dialects.postgresql import UUID

class UserInputModel(BaseModel):
    username: str
    email: str
    password: str