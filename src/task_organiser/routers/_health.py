from fastapi import APIRouter

from task_organiser.schemas import HealthResponse, HealthResponseStatus

router = APIRouter(prefix="/health")


@router.get("")
def get_health() -> HealthResponse:
    return HealthResponse(status=HealthResponseStatus.up)
