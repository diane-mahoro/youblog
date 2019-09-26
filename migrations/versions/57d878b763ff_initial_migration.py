"""Initial Migration

Revision ID: 57d878b763ff
Revises: ac270bd74fc0
Create Date: 2019-09-22 00:55:25.024972

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '57d878b763ff'
down_revision = 'ac270bd74fc0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('description', sa.String(), nullable=True))
    op.drop_column('pitches', 'pitch')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('pitch', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('pitches', 'description')
    # ### end Alembic commands ###
