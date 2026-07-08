from typing import Annotated

from fastapi import APIRouter, Depends, status

from task_organiser import schemas, services

router = APIRouter(prefix="/auth")


@router.post("/signin", status_code=status.HTTP_200_OK)
def signin(
    request: schemas.SigninRequest, auth_service: Annotated[services.Auth, Depends(services.Auth)]
) -> schemas.SigninResponse:
    return auth_service.signin(request)


@router.post("/signup", status_code=status.HTTP_201_CREATED, summary="Register a new user")
def signup(
    request: schemas.SignupRequest, auth_service: Annotated[services.Auth, Depends(services.Auth)]
) -> schemas.SignupResponse:
    return auth_service.signup(request)
