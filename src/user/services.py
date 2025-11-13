from fastapi import HTTPException, status
from src.database.core import DBSession
from src.user import models
from src.entites.user import UserDB

def get_all_users(db: DBSession):
    return db.query(UserDB).all()

def create_user(request: models.User, db: DBSession):
    new_user = UserDB(name = request.name, email = request.email, password = request.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
    
def get_user(name: str, db: DBSession):
    user = db.query(UserDB).filter(UserDB.name == name).first()
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f"User name {name} not found")
    return user

def update_user(name: str, request: models.User, db: DBSession):
    user = db.query(UserDB).filter(UserDB.name == name)
    if not user.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f"User name {name} not found")

    user.update({"name": request.name, "email": request.email, "password": request.password})
    db.commit()
    return {"Details": f"Updated user name {name} with request record successfully"} 

def delete_user(name: str, db: DBSession):
    user = db.query(UserDB).filter(UserDB.name == name)
    if not user.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f"User name {name} not found")
    
    user.delete()
    db.commit()
    return {"Details": f"User name {name} record got deleted successfully "}
