from fastapi import APIRouter, status, HTTPException, Response
import model

router = APIRouter(
    prefix = "/user",
    tags = ["User Registation and Authentication"]
)

users : list[model.User] = []

@router.post("", status_code=status.HTTP_201_CREATED)
async def create(request : model.User):
    users.append(request)
    return {"New user is been added to the list"}

@router.get("", status_code=status.HTTP_200_OK)
async def get_all_user():
    return users

@router.get("/{name}", status_code=status.HTTP_200_OK)
async def get_user(name: str):
    for user in users:
        if user.name == name:
            return user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User: {name} not found!")


@router.put("/{name}", status_code=status.HTTP_202_ACCEPTED)
async def update_user(name: str, request:model.User):
    for index, user in enumerate(users):
        if user.name == name:
            users[index] = request
            return users
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User: {name} not found!")

@router.delete("/{name}", status_code=status.HTTP_202_ACCEPTED)
async def remove_user(name: str):
    for index, user in enumerate(users):
        if user.name == name:
            users.pop(index)
            return users
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User: {name} not found!") 