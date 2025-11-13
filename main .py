from fastapi import FastAPI
from user import routers

app = FastAPI()

app.include_router(routers.router)