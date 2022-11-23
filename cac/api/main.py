from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from passlib.hash import bcrypt
from datetime import date
from uuid import uuid4
import jwt

from cac.api.dependencies import get_db
from cac.api.models.users import UserInputModel
from cac.api.schemas.users import Users

api_signature = 'carsandcoffeeapiv1'

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

async def authenticate_user(username: str, password: str):
    user = Users.get(username=username)
    if not user:
        return False
    if not user.verify_password(password):
        return False
    return user

@app.post("/client/login")
async def generate_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(form_data.username, form_data.password)

    if not user:
        return {"error": "invalid credentials"}

    token = jwt.encode(user.dict(), api_signature)

    return {"access_token": token, "token_type": "bearer"}

@app.post("/")
async def create_user(input: UserInputModel, db: Session = Depends(get_db)):
    new_uuid = uuid4()
    to_create = Users(
        id=new_uuid,
        username=input.username,
        email=input.email,
        password=bcrypt.hash(input.password),
        creation_date=date.today()
    )
    db.add(to_create)
    db.commit()
    return {"success": True}
    

@app.get("/")
async def get_user_by_username(username: str, db: Session = Depends(get_db)):
    return db.query(Users).filter(Users.username == username).first()

@app.delete("/")
async def delete_user_by_username(username: str, db: Session = Depends(get_db)):
    db.query(Users).filter(Users.username == username).delete()
    db.commit()
    return {"success": True}
