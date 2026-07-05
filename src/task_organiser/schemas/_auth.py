from pydantic import BaseModel, Field


class SignupRequest(BaseModel):
    user_name: str
    password: str = Field(min_length=8)


class SignupResponse(BaseModel):
    pass
