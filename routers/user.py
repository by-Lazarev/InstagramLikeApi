from fastapi import APIRouter, Depends
from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session

from routers.schemas import UserDisplay, UserBase
from db.database import get_db
from db import db_user
from db.models import DbUser

router = APIRouter(
    prefix="/user",
    tags=["user"]
)


# ---[CRUD]---
# ---[CREATE]---
@router.post("/", response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    if db.query(DbUser).filter(DbUser.email == request.email).first():
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You already have an account"
        )
    if db.query(DbUser).filter(DbUser.username == request.username).first():
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="This name is already used, try the other one"
        )
    return db_user.create_user(request, db)
