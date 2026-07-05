from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from task_organiser import settings

engine = create_engine(settings.settings.database_url, echo=True)
DB = sessionmaker(engine, autoflush=False)


def get_db() -> Generator[Session]:
    db = DB()
    try:
        yield db
    finally:
        db.close()


class Base(DeclarativeBase):
    pass
