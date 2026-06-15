from fastapi import APIRouter, Depends, status
from src.tasks import controller
from src.tasks.dtos import TaskSchema, TaskResponseSchema
from src.utils.db import get_db

from typing import List

task_routes = APIRouter(prefix="/tasks")


@task_routes.post(
    "/create", response_model=TaskResponseSchema, status_code=status.HTTP_201_CREATED
)
def create_task(body: TaskSchema, db=Depends(get_db)):
    return controller.create_task(body, db)


@task_routes.get(
    "/all_task", response_model=List[TaskResponseSchema], status_code=status.HTTP_200_OK
)
def get_all_tasks(db=Depends(get_db)):
    return controller.get_tasks(db)


@task_routes.get(
    "/task/{_id}", response_model=TaskResponseSchema, status_code=status.HTTP_200_OK
)
def get_one_task(_id: int, db=Depends(get_db)):
    return controller.get_one_task(_id, db)


@task_routes.put(
    "/update/{_id}",
    response_model=TaskResponseSchema,
    status_code=status.HTTP_201_CREATED,
)
def update_task(body: TaskSchema, _id: int, db=Depends(get_db)):
    return controller.update_task(body, _id, db)


@task_routes.delete("/delete/{_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(_id: int, db=Depends(get_db)):
    return controller.delete_task(_id, db)
