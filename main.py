from fastapi import FastAPI

from src.utils.db import Base, engine

# define user task table
# from src.tasks.models import TaskModel

# connect routes with server
from src.tasks.router import task_routes
from src.user.router import user_routes

Base.metadata.create_all(engine)

APP = FastAPI(
    title='Task app'
)

# task route
APP.include_router(task_routes)
APP.include_router(user_routes)