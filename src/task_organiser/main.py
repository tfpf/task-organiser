from fastapi import FastAPI

import task_organiser
from task_organiser import routers
from task_organiser import database

from task_organiser import models

database.Base.metadata.create_all(database.engine)

app = FastAPI(title=task_organiser.__name__, version=task_organiser.__version__)
app.include_router(routers.auth_router)
app.include_router(routers.health_router)
