import os
from sqlalchemy import create_engine, Column, MetaData

from clickhouse_sqlalchemy import (
    make_session,
    get_declarative_base,
    types,
    engines,
)

clickhouse_host = os.environ.get("CLICKHOUSE_HOST", "localhost")
uri = f"clickhouse://default:@{clickhouse_host}:8123/default"
engine = create_engine(uri)
session = make_session(engine)
metadata = MetaData(bind=engine)


Base = get_declarative_base(metadata=metadata)


class Seller(Base):
    """Модель для БД."""
    posting_number = Column(types.String, primary_key=True)
    number_etgb = Column(types.String)
    date_etgb = Column(types.String)
    url_etgb = Column(types.String)

    __table_args__ = (engines.Memory(),)
