from argparse import ArgumentParser
from pathlib import Path

import uvicorn
from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError

import task_organiser
from task_organiser import (
    database,
    models,  # noqa: F401
    routers,
)

argument_parser = ArgumentParser()
argument_parser.add_argument("--reload", action="store_true", help="enable auto-reload (forwarded to Uvicorn)")
args = argument_parser.parse_args()

database.Base.metadata.create_all(database.engine)

app = FastAPI(title=task_organiser.__name__, version=task_organiser.__version__)
app.include_router(routers.auth_router)
app.include_router(routers.health_router)


@app.exception_handler(IntegrityError)
async def handle_integrity_error(_request: Request, e: IntegrityError) -> JSONResponse:
    match e.orig.diag.constraint_name:
        case "users_user_name_unique":
            status_code = status.HTTP_409_CONFLICT
            text = "User name is already taken"
        case _:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            text = "Unknown constraint violation error"
    return JSONResponse(status_code=status_code, content={"text": text})


def main():
    uvicorn.run("task_organiser.main:app", reload=args.reload, reload_dirs=[Path(__file__).parent])


if __name__ == "__main__":
    main()
