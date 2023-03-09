from fastapi import APIRouter, Depends
from fastapi import HTTPException, status
from fastapi import File, UploadFile
from sqlalchemy.orm import Session
from random import choice
from string import ascii_letters
from shutil import copyfileobj

from db import db_post
from db.database import get_db
from routers.schemas import PostDisplay, PostBase, UserAuth
from auth.oauth2 import get_current_user

router = APIRouter(
    prefix="/post",
    tags=["post"]
)

image_url_types = ("absolute", "relative")


# ---[CRUD]---
# ---[CREATE]---
@router.post("", response_model=PostDisplay)
def create_post(request: PostBase, db: Session = Depends(get_db), current_user: UserAuth = Depends(get_current_user)):
    if request.image_url_type not in image_url_types:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="url_type are not correct, only absolute or relative are allowed"
        )
    return db_post.create_post(request, db)


@router.post("/image")
def upload_image(image: UploadFile = File(...), current_user: UserAuth = Depends(get_current_user)):
    rand_str = ''.join(choice(ascii_letters) for _ in range(6))
    filename = f"_{rand_str}.".join(image.filename.rsplit(".", 1))
    path = f"images/{filename}"

    with open(path, "w+b") as local_file:
        copyfileobj(image.file, local_file)

    return {"filename": path}


# ---[READ]---
@router.get("/all", response_model=list[PostDisplay])
def read_all_posts(db: Session = Depends(get_db)):
    return db_post.get_all(db)


# ---[UPDATE]---

# ---[DELETE]---
@router.delete("/delete/{post_id}")
def delete_post(post_id: int, db: Session = Depends(get_db), current_user: UserAuth = Depends(get_current_user)):
    return db_post.delete_post(post_id, db, current_user.id)
