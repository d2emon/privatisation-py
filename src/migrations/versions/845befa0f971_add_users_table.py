"""Add users table

Revision ID: 845befa0f971
Revises: 5d07b228b962
Create Date: 2020-05-29 23:52:37.162981

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '845befa0f971'
down_revision = '5d07b228b962'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('login', sa.String(length=16), nullable=True),
    sa.Column('password', sa.String(length=128), nullable=True),
    sa.Column('name', sa.String(length=32), nullable=True),
    sa.Column('surname', sa.String(length=32), nullable=True),
    sa.Column('role', sa.SmallInteger(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_login'), 'user', ['login'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_login'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
