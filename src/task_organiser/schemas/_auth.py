from pydantic import BaseModel, Field


class SignupRequest(BaseModel):
    username: str
    password: str = Field(min_length=8)


class SignupResponse(BaseModel):
    pass
