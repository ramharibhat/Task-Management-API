from fastapi import APIRouter, status
from src.user import models, services
from src.database.core import DBSession
from typing import List

router = APIRouter(
    prefix = "/user",
    tags = ["User Registation and Authentication"]
)

@router.post("", response_model=models.User, status_code=status.HTTP_201_CREATED)
async def create(request: models.User, db: DBSession):
    return services.create_user(request, db)

@router.get("", response_model=List[models.User], status_code=status.HTTP_200_OK)
async def get_all_user(db: DBSession):
    return services.get_all_users(db)

@router.get("/{name}", response_model=models.User, status_code=status.HTTP_200_OK)
async def get_user(name: str, db: DBSession):
    return services.get_user(name, db)

@router.put("/{name}", status_code=status.HTTP_202_ACCEPTED)
async def update_user(name: str, request:models.User, db: DBSession):
    return services.update_user(name, request, db)

@router.delete("/{name}", status_code=status.HTTP_202_ACCEPTED)
async def remove_user(name: str, db: DBSession):
   return services.delete_user(name, db)