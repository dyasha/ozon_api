import os

from clickhouse_sqlalchemy import engines, get_declarative_base, make_session, types
from sqlalchemy import Column, MetaData
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

clickhouse_host = os.environ.get("CLICKHOUSE_HOST", "localhost")
# uri = f"clickhouse://default:@{clickhouse_host}:8123/default"
uri = f"clickhouse+asynch://default:@{clickhouse_host}:9000/default"
# engine = create_engine(uri)
engine = create_async_engine(uri, echo=True)
session = make_session(engine, is_async=True)
metadata = MetaData(bind=engine)
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession)


Base = get_declarative_base(metadata=metadata)


async def get_async_session():
    async with AsyncSessionLocal() as async_session:
        yield async_session


class Seller(Base):
    """Модель для БД."""

    posting_number = Column(types.Int)
    number_etgb = Column(types.String)
    date_etgb = Column(types.Date, primary_key=True)
    url_etgb = Column(types.String)
    timestamp = Column(types.DateTime)

    __table_args__ = (engines.ReplacingMergeTree(order_by=posting_number),)
