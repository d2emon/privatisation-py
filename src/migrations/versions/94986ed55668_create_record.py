"""create_record

Revision ID: 94986ed55668
Revises:
Create Date: 2017-03-14 16:12:20.380787

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '94986ed55668'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('record',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.Column('reg_num', sa.Integer(), nullable=True),
    sa.Column('reg_id', sa.String(length=8), nullable=True),
    sa.Column('city_id', sa.Integer(), nullable=True),
    sa.Column('addr_type', sa.Integer(), nullable=True),
    sa.Column('addr_name', sa.String(length=64), nullable=True),
    sa.Column('addr_build', sa.String(length=8), nullable=True),
    sa.Column('addr_flat', sa.String(length=16), nullable=True),
    sa.Column('owner', sa.String(length=64), nullable=True),
    sa.Column('owner_init', sa.String(length=8), nullable=True),
    sa.Column('base_id', sa.String(length=8), nullable=True),
    sa.Column('base_date', sa.Date(), nullable=True),
    sa.Column('reg_date', sa.Date(), nullable=True),
    sa.Column('comment', sa.UnicodeText(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('record')
    # ### end Alembic commands ###
