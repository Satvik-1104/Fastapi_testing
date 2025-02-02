from fastapi import FastAPI
import models
import database
from .routers import blog, user, authentication


app = FastAPI()  # importing FastAPI

models.Base.metadata.create_all(bind=database.engine)  # Creating the Backend Engine

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)
