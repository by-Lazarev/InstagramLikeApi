from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from db import models
from db.database import engine

from routers import user, post
from auth import authentication

app = FastAPI()

models.Base.metadata.create_all(engine)
app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(post.router)

app.mount("/images", StaticFiles(directory="images"), name="images")


@app.get("/")
async def root():
    return {"message": "Hello World"}
