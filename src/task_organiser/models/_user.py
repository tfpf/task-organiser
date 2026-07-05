from sqlalchemy import String, UUID, BINARY
from sqlalchemy.orm import Mapped, mapped_column

from task_organiser.database import Base

class User(Base):
    __tablename__ = "users"
    id: Mapped[UUID] = mapped_column(primary_key=True)
    user_name: Mapped[str] = mapped_column(String(255), index=True, unique=True)
    password_hash: Mapped[str] = mapped_column(String(255))
