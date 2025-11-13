from fastapi import FastAPI
from src.user import routers as user_routers
from src.tasks import routers as tasks_routers
from src.database.core import Base, engine

app = FastAPI()

Base.metadata.create_all(engine)

app.include_router(user_routers.router)
app.include_router(tasks_routers.router)
