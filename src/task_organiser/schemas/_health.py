import enum

from pydantic import BaseModel

HealthResponseStatus = enum.StrEnum("HealthResponseStatus", ["up"])


class HealthResponse(BaseModel):
    status: HealthResponseStatus
