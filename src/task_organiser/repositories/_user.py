from sqlalchemy.orm import Session

from task_organiser import models


class User:
    def __init__(self, db: Session):
        self.db = db

    def create(self, user_name: str, password_hash: bytes):
        user_model = models.User(user_name=user_name, password_hash=password_hash)
        self.db.add(user_model)
