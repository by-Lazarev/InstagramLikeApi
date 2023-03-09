from fastapi import APIRouter, Depends, HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm.session import Session

from db.database import get_db
from db.models import DbUser
from db import hash
from auth import oauth2

router = APIRouter(
    tags=["authentication"]
)


@router.post("/login")
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(DbUser).filter(DbUser.username == request.username).first()
    if not user:
        raise HTTPException(status_code=404, detail="Invalid credentials")
    if not hash.verify(user.password, request.password):
        raise HTTPException(status_code=404, detail="Incorrect name or password")

    access_token = oauth2.create_access_token(data={"username": user.username})

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user_id": user.id,
        "username": user.username
    }
