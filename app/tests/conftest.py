import pytest
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker

from app.settings import settings
from app.database import Base
from app.models import Request


@pytest.fixture(scope="session")
def engine():
    return create_async_engine(settings.pg_url_asyncpg)


@pytest.fixture(scope="session")
async def tables(engine):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        yield
        await conn.run_sync(Base.metadata.drop_all)


@pytest.fixture
def db_session(engine, tables):
    connection = engine.connect()
    transaction = connection.begin()
    session = async_sessionmaker(bind=engine)()
    yield session
    session.close()
    transaction.rollback()
    connection.close()