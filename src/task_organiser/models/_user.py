import uuid

from sqlalchemy import BINARY, String
from sqlalchemy.orm import Mapped, mapped_column

from task_organiser import database


class User(database.Base):
    __tablename__: str = "users"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    user_name: Mapped[str] = mapped_column(String(255), index=True, unique=True)
    password_hash: Mapped[BINARY] = mapped_column(String(255))
