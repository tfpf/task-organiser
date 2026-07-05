from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from task_organiser import constants, database, repositories, schemas


class Auth:
    def __init__(self, db: Annotated[Session, Depends(database.get_db)]):
        self.db = db
        self.user_repository = repositories.User(self.db)

    def signup(self, request: schemas.SignupRequest) -> schemas.SignupResponse:
        self.user_repository.create(user_name=request.user_name, password_hash=request.password)
        self.db.commit()
        return schemas.SignupResponse(text=constants.Auth.signup_success)
