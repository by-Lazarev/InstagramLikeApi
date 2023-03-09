from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

from db import db_comment
from db.database import get_db
from routers.schemas import CommentBase, UserAuth
from auth.oauth2 import get_current_user

router = APIRouter(
    prefix="/comment",
    tags=["comment"]
)


# ---[CRUD]---


# ---[CREATE]---
@router.post("")
def create_comment(
        request: CommentBase,
        db: Session = Depends(get_db),
        current_user: UserAuth = Depends(get_current_user)
):
    return db_comment.create_comment(db, request)


# ---[READ]---
@router.get("/{post_id}/all")
def read_all_comments(post_id: int, db: Session = Depends(get_db)):
    return db_comment.read_all_comments(post_id, db)
# ---[UPDATE]---
# ---[DELETE]---
