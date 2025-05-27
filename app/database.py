
from sqlalchemy.ext.declarative import  declarative_base
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker , declarative_base
from app.config import Config

# DATABASE_URL= 'postgresql://{username}:{password}@localhost:{port_no_that_used_postgresql}/{databaseName}'
DATABASE_URL = f"postgresql+asyncpg://{Config.DB_USER}:{Config.DB_PASS}@localhost:5433/{Config.DB_NAME}"

engine = create_async_engine(DATABASE_URL, echo=True)

async_session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()



# Quick setup: create all tables based on your models.
async def init_db():
    async with engine.begin() as conn:
        # This will create all tables which do not yet exist.
        await conn.run_sync(Base.metadata.create_all)


async def get_db():
    async with async_session() as session:
        yield session
