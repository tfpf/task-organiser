import enum

from pydantic import BaseModel, Field


class SigninResponseTokenType(enum.StrEnum):
    BEARER = enum.auto()


class SigninResponse(BaseModel):
    access_token: str
    expires_at: int
    token_type: SigninResponseTokenType = SigninResponseTokenType.BEARER


class SignupRequest(BaseModel):
    username: str
    password: str = Field(min_length=8)


class SignupResponse(BaseModel):
    pass
