from fastapi import FastAPI
from src.utils.db import Base, engine

Base.metadata.create_all(engine)

APP = FastAPI(
    title='Task app'
)