from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
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


def commit_db(db: Session):
    try:
        db.commit()
    except SQLAlchemyError:
        db.rollback()
        raise


class Base(DeclarativeBase):
    pass
