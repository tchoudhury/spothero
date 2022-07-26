"""First revision

Revision ID: e76e8615fc6d
Revises: 
Create Date: 2022-07-24 20:06:38.837589

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'e76e8615fc6d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("Rates",
                    sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
                    sa.Column("days", sa.Text),
                    sa.Column("start_time", sa.Time),
                    sa.Column("end_time", sa.Time),
                    sa.Column("timezone", sa.Text),
                    sa.Column("price", sa.Numeric(10, 2)),
                    sa.UniqueConstraint('days', 'start_time', "end_time", name='times_constraint')
    )


def downgrade() -> None:
    op.drop_table('Rates')
