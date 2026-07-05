from fastapi import APIRouter

from task_organiser import schemas

router = APIRouter(prefix="/health")


@router.get("")
def get_health() -> schemas.HealthResponse:
    return schemas.HealthResponse(status=schemas.HealthResponseStatus.UP)
