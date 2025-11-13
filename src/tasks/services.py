from fastapi import HTTPException, status
from src.database.core import DBSession
from src.tasks import models
from src.entites.tasks import TaskDB
from src.entites.user import UserDB

def get_all_tasks(db: DBSession):
    return db.query(TaskDB).all()

def create_task(request: models.Task, db: DBSession):
    # get the user db entry 
    task_user = db.query(UserDB).filter(UserDB.name == request.user.name).first()
    if not task_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User name {request.user.name} is not found")
    new_task = TaskDB(title = request.title, 
                      description = request.description, 
                      is_completed = request.is_completed, 
                      creation_date = request.creation_date,
                      user = task_user
                    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task
    
def get_task(title: str, db: DBSession):
    task = db.query(TaskDB).filter(TaskDB.title == title).first()
    if not task:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f"Task title {title} not found")
    return task

def update_task(title: str, request: models.Task, db: DBSession):
    task = db.query(TaskDB).filter(TaskDB.title == title).first()
    if not task:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f"Task title {title} not found")

    task_user = db.query(UserDB).filter(UserDB.name == request.user.name).first()
    if not task_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User name {request.user.name} is not found")

    task.title = request.title # type:ignore
    task.description = request.description # type:ignore
    task.is_completed = request.is_completed # type:ignore
    task.creation_date = request.creation_date # type:ignore
    task.user = task_user
    db.commit()
    return {"Details": f"Updated task title {title} with request record successfully"} 

def delete_task(title: str, db: DBSession):
    task = db.query(TaskDB).filter(TaskDB.title == title)
    if not task.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f"Task title {title} not found")
    
    task.delete()
    db.commit()
    return {"Details": f"Task title {title} record got deleted successfully "}
