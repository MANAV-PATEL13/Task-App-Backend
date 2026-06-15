from fastapi import FastAPI

from src.utils.db import Base, engine

# define user task table
from src.tasks.models import TaskModel

Base.metadata.create_all(engine)

APP = FastAPI(
    title='Task app'
)