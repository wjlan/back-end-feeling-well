"""empty message

Revision ID: 8c2fa5587992
Revises: 
Create Date: 2023-02-01 14:06:49.899434

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8c2fa5587992'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('account',
    sa.Column('account_id', sa.Integer(), autoincrement=True, nullable=True),
    sa.Column('account_uid', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('account_uid')
    )
    op.create_table('word',
    sa.Column('word_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('account_uid', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['account_uid'], ['account.account_uid'], ),
    sa.PrimaryKeyConstraint('word_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('word')
    op.drop_table('account')
    # ### end Alembic commands ###