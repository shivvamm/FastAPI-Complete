from fastapi import APIRouter,Depends,HTTPException,Body,Path,Query
from settings import SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session
from models import Users
from starlette import status
from pydantic import BaseModel,Field
from .auth import get_current_user
from passlib.context import CryptContext

router = APIRouter(
     prefix="/users",
    tags=['users']
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session,Depends(get_db)]
user_dependency = Annotated[dict,Depends(get_current_user)]
bcrypt_context  = CryptContext(schemes=['bcrypt'],deprecated='auto')



class UserVerification(BaseModel):
    password: str
    new_password: str = Field(min_length=6)


@router.get("/",status_code=status.HTTP_200_OK)
async def get_user(user:user_dependency,db:db_dependency):
    if user is None:
        raise HTTPException(status_code=401,detail="Authentication Failed")

    user_data = db.query(Users).filter(Users.username == user.get('username')).first()
    return user_data


@router.put("/password",status_code=status.HTTP_204_NO_CONTENT)
async def change_password(user:user_dependency,db:db_dependency,user_verification:UserVerification):
    if user is None:
        raise HTTPException(status_code=401,detail="Authentication Failed")

    user_model = db.query(Users).filter(Users.id == user.get('id')).first()

    if not bcrypt_context.verify(user_verification.password,user_model.hashed_password):
        raise HTTPException(status_code=401,detail="Error No password cahnged")
    
    user_model.hashed_password = bcrypt_context.hash(user_verification.new_password)
    db.add(user_model)
    db.commit()

