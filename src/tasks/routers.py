from fastapi import APIRouter, status
from src.tasks import models, services
from src.database.core import DBSession
from typing import List

router = APIRouter(
    prefix = "/task",
    tags = ["Task Management"]
)

@router.post("", response_model=models.Task, status_code=status.HTTP_201_CREATED)
async def create_task(request: models.Task, db: DBSession):
    return services.create_task(request, db)

@router.get("", response_model=List[models.Task], status_code=status.HTTP_200_OK)
async def get_all_tasks(db: DBSession):
    return services.get_all_tasks(db)

@router.get("/{title}", response_model=models.Task, status_code=status.HTTP_200_OK)
async def get_task(title: str, db: DBSession):
    return services.get_task(title, db)

@router.put("/{title}", status_code=status.HTTP_202_ACCEPTED)
async def update_task(title: str, request:models.Task, db: DBSession):
    return services.update_task(title, request, db)

@router.delete("/{title}", status_code=status.HTTP_202_ACCEPTED)
async def remove_task(title: str, db: DBSession):
   return services.delete_task(title, db)