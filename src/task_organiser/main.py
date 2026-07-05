from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError

import task_organiser
from task_organiser import (
    database,
    models,  # noqa: F401
    routers,
)

database.Base.metadata.create_all(database.engine)

app = FastAPI(title=task_organiser.__name__, version=task_organiser.__version__)
app.include_router(routers.auth_router)
app.include_router(routers.health_router)


@app.exception_handler(IntegrityError)
async def handle_integrity_error(_request: Request, _e: IntegrityError):
    return JSONResponse(status_code=status.HTTP_409_CONFLICT, content={"text": "database constraint violation"})
