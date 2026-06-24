from fastapi import APIRouter, Depends, status
from src.tasks import controller
from src.tasks.dtos import TaskSchema, TaskResponseSchema
from src.utils.db import get_db

from typing import List


from src.utils.helpers import is_authenticated
from src.user.models import UserModel

task_routes = APIRouter(prefix="/tasks")


@task_routes.post(
    "/create", response_model=TaskResponseSchema, status_code=status.HTTP_201_CREATED
)
def create_task(body: TaskSchema, db=Depends(get_db), user:UserModel = Depends(is_authenticated)):
    return controller.create_task(body, db, user)


@task_routes.get(
    "/all_task", response_model=List[TaskResponseSchema], status_code=status.HTTP_200_OK
)
def get_all_tasks(db=Depends(get_db), user:UserModel = Depends(is_authenticated)):
    return controller.get_tasks(db, user)


@task_routes.get(
    "/task/{_id}", response_model=TaskResponseSchema, status_code=status.HTTP_200_OK
)
def get_one_task(_id: int, db=Depends(get_db), user:UserModel = Depends(is_authenticated)):
    return controller.get_one_task(_id, db)


@task_routes.put(
    "/update/{_id}",
    response_model=TaskResponseSchema,
    status_code=status.HTTP_201_CREATED,
)
def update_task(body: TaskSchema, _id: int, db=Depends(get_db), user:UserModel = Depends(is_authenticated)):
    return controller.update_task(body, _id, db, user)


@task_routes.delete("/delete/{_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(_id: int, db=Depends(get_db), user:UserModel = Depends(is_authenticated)):
    return controller.delete_task(_id, db, user)
