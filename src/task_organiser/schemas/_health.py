import enum

from pydantic import BaseModel


class HealthResponseStatus(enum.StrEnum):
    UP = enum.auto()


class HealthResponse(BaseModel):
    status: HealthResponseStatus
