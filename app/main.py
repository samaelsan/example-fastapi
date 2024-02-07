from fastapi import FastAPI
from . import models
from .database import engine
from .routers import post, user, auth, vote
from .config import settings
from fastapi.middleware.cors import CORSMiddleware


print(settings.database_username)
#models.Base.metadata.create_all(bind=engine) ###Not require because using alembic

app = FastAPI(
    title="MY FIRST API"
)

origins = ["*"]     
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
def root():
    return{"message": "Welcome to my API successfully deployed from a CI/CD pipeline!"}





