from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from ..config import settings
from sqlalchemy import NullPool

if settings.MODE == "TEST":
    DATABASE_URL = settings.TEST_DB_URL
    DATABASE_PARAMS = {"poolclass": NullPool}
else:
    DATABASE_PARAMS = {}
    DATABASE_URL = settings.DB_URL

engine = create_async_engine(
    DATABASE_URL,
    **DATABASE_PARAMS,
    echo=True
    )

async_session_maker = async_sessionmaker(engine)

class Base(DeclarativeBase):
    pass
