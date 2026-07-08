import uuid

from sqlalchemy import Constraint, String, UniqueConstraint, Uuid, text
from sqlalchemy.orm import Mapped, mapped_column

from task_organiser import database


class User(database.Base):
    __tablename__: str = "users"
    __table_args__: tuple[Constraint] = (UniqueConstraint("username", name="users_username_unique"),)

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, server_default=text("gen_random_uuid()"))
    username: Mapped[str] = mapped_column(String(255))
    password_hash: Mapped[str] = mapped_column(String(255))
