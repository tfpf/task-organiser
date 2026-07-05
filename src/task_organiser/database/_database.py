from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from task_organiser import settings

engine = create_engine(settings.settings.database_url, echo=True)
Session = sessionmaker(bind=engine, autoflush=False)


class Base(DeclarativeBase):
    pass
