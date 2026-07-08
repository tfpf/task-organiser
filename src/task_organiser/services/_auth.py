from typing import Annotated

from argon2 import PasswordHasher
from fastapi import Depends
from sqlalchemy.orm import Session

from task_organiser import database, repositories, schemas

password_hasher = PasswordHasher()


class Auth:
    def __init__(self, db: Annotated[Session, Depends(database.get_db)]):
        self.db = db
        self.user_repository = repositories.User(self.db)

    def signup(self, request: schemas.SignupRequest) -> schemas.SignupResponse:
        password_hash = password_hasher.hash(request.password)
        self.user_repository.create(username=request.username, password_hash=password_hash)
        database.commit_db(self.db)
        return schemas.SignupResponse()
