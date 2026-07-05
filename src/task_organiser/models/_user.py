import uuid

from sqlalchemy import String, Uuid, text
from sqlalchemy.orm import Mapped, mapped_column

from task_organiser import database


class User(database.Base):
    __tablename__: str = "users"
    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, server_default=text("gen_random_uuid()"))
    user_name: Mapped[str] = mapped_column(String(255), index=True, unique=True)
    password_hash: Mapped[str] = mapped_column(String(255))
