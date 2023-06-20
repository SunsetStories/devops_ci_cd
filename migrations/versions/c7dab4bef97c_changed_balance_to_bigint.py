"""changed balance to bigint

Revision ID: c7dab4bef97c
Revises: 1e69b97662a5
Create Date: 2023-05-15 22:48:03.403377

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c7dab4bef97c'
down_revision = '1e69b97662a5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('transactions_table', schema=None) as batch_op:
        batch_op.alter_column('amount',
               existing_type=sa.INTEGER(),
               type_=sa.BigInteger(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('transactions_table', schema=None) as batch_op:
        batch_op.alter_column('amount',
               existing_type=sa.BigInteger(),
               type_=sa.INTEGER(),
               existing_nullable=True)

    # ### end Alembic commands ###
