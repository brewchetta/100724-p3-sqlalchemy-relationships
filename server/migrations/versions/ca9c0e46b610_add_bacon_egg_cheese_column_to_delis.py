"""add bacon_egg_cheese column to delis

Revision ID: ca9c0e46b610
Revises: 445d8ad5bb65
Create Date: 2024-12-03 10:41:37.744442

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ca9c0e46b610'
down_revision = '445d8ad5bb65'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('delis_table', schema=None) as batch_op:
        batch_op.add_column(sa.Column('bacon_egg_cheese', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('delis_table', schema=None) as batch_op:
        batch_op.drop_column('bacon_egg_cheese')

    # ### end Alembic commands ###
