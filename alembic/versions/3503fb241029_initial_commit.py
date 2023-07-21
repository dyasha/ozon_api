"""Initial commit

Revision ID: 3503fb241029
Revises:
Create Date: 2023-07-21 16:19:26.748435

"""
import clickhouse_sqlalchemy
import sqlalchemy as sa
from clickhouse_sqlalchemy import engines

from alembic import op

# revision identifiers, used by Alembic.
revision = '3503fb241029'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('seller',
    sa.Column('posting_number', clickhouse_sqlalchemy.types.common.Int(), nullable=True),
    sa.Column('number_etgb', clickhouse_sqlalchemy.types.common.String(), nullable=True),
    sa.Column('date_etgb', clickhouse_sqlalchemy.types.common.Date(), nullable=False),
    sa.Column('url_etgb', clickhouse_sqlalchemy.types.common.String(), nullable=True),
    sa.Column('timestamp', clickhouse_sqlalchemy.types.common.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('date_etgb'),
    engines.ReplacingMergeTree(order_by='posting_number')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('seller')
    # ### end Alembic commands ###
