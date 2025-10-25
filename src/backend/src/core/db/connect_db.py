from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase
from ..config import settings

DATABASE_URL = settings.DB_URL

engine = create_async_engine(
    DATABASE_URL,
    echo=True
)

async_session = async_sessionmaker(engine)

class Base(DeclarativeBase):
    pass