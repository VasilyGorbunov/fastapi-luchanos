from typing import Generator

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

import settings

engine = create_async_engine(settings.REAL_DATABASE_URL, future=True, echo=True)
async_session = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession, )


async def get_db() -> Generator:
    """Dependency for getting async session"""
    try:
        session: AsyncSession = async_session()
        yield session
    finally:
        await session.close()
