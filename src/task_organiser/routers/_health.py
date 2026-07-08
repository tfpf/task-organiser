from fastapi import APIRouter, status

from task_organiser import schemas

router = APIRouter(prefix="/health")


@router.get("", status_code=status.HTTP_200_OK)
def health() -> schemas.HealthResponse:
    return schemas.HealthResponse(status=schemas.HealthResponseStatus.UP)
