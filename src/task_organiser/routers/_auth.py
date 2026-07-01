from typing import Annotated

from fastapi import APIRouter, Depends, status

from task_organiser.schemas import SignupRequest, SignupResponse
from task_organiser.services import AuthService

router = APIRouter(prefix="/auth")


@router.post("/signup", status_code=status.HTTP_201_CREATED)
def signup(request: SignupRequest, auth_service: Annotated[AuthService, Depends(AuthService)]) -> SignupResponse:
    return auth_service.signup(request)
