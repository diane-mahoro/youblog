"""Initial Migration

Revision ID: af21ded3282c
Revises: d6c1e9f6a0eb
Create Date: 2019-09-20 16:19:15.177953

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'af21ded3282c'
down_revision = 'd6c1e9f6a0eb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('pitch', sa.String(), nullable=True))
    op.drop_column('pitches', 'posted')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('posted', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.drop_column('pitches', 'pitch')
    # ### end Alembic commands ###
