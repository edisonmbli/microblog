"""add language to posts

Revision ID: 744a248e03ba
Revises: 094535637bf4
Create Date: 2018-01-25 08:08:57.236146

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '744a248e03ba'
down_revision = '094535637bf4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('language', sa.String(length=5), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'language')
    # ### end Alembic commands ###
