from fastapi import HTTPException
from sqlalchemy.orm.session import Session
from datetime import datetime

from routers.schemas import CommentBase
from db.models import DbComment


# ---[CRUD]---

# ---[CREATE]---
def create_comment(db: Session, request: CommentBase):
    new_comment = DbComment(
        text=request.text,
        username=request.username,
        timestamp=datetime.now(),
        post_id=request.post_id
    )
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment


# ---[READ]---
def read_all_comments(post_id: int, db: Session):
    return db.query(DbComment).filter(DbComment.post_id == post_id).all()
# ---[UPDATE]---
# ---[DELETE]---
