from fastapi import HTTPException
from sqlalchemy.orm.session import Session
from datetime import datetime

from routers.schemas import PostBase
from db.models import DbPost


def create_post(request: PostBase, db: Session):
    new_post = DbPost(
        image_url=request.image_url,
        image_url_type=request.image_url_type,
        caption=request.caption,
        timestamp=datetime.now(),
        user_id=request.creator_id
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


def get_all(db: Session):
    return db.query(DbPost).all()


def delete_post(post_id: int, db: Session, current_user: int):
    post = db.query(DbPost).filter(DbPost.id == post_id).first()
    if not post:
        raise HTTPException(
            status_code=404,
            detail=f"Post with id {post_id} not found"
        )
    if post.user_id != current_user:
        raise HTTPException(
            status_code=403,
            detail=f"Only post creator can delete post"
        )

    db.delete(post)
    db.commit()
    return {"msg": f"post with id {post_id} deleted"}
