from typing import Annotated

from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from task_organiser import schemas, services

oauth2_scheme = OAuth2PasswordBearer("/auth/signin")
router = APIRouter(prefix="/auth")

@router.get("/me", status_code=status.HTTP_200_OK, summary="View currently logged-in user")
def me(token: Annotated[str, Depends(oauth2_scheme)]):
    return {}


@router.post("/signin", status_code=status.HTTP_200_OK, summary="Log in")
def signin(
    request: Annotated[OAuth2PasswordRequestForm, Depends()],
    auth_service: Annotated[services.Auth, Depends(services.Auth)],
) -> schemas.SigninResponse:
    return auth_service.signin(request)


@router.post("/signup", status_code=status.HTTP_201_CREATED, summary="Register a new user")
def signup(
    request: schemas.SignupRequest, auth_service: Annotated[services.Auth, Depends(services.Auth)]
) -> schemas.SignupResponse:
    return auth_service.signup(request)
