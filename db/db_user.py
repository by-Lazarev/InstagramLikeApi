from sqlalchemy.orm.session import Session

from routers.schemas import UserBase
from db.models import DbUser
from db import hash


def create_user(request: UserBase, db: Session):
    new_user = DbUser(
        username=request.username,
        email=request.email,
        password=hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
