"""created fakultas table

Revision ID: 55e13b565dea
Revises: e8356e7ebccc
Create Date: 2021-06-27 16:58:57.292914

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '55e13b565dea'
down_revision = 'e8356e7ebccc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('fakultas',
    sa.Column('id_fakultas', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('kode_fakultas', sa.String(length=250), nullable=False),
    sa.Column('nama_fakultas', sa.String(length=250), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id_fakultas')
    )
    op.create_index(op.f('ix_fakultas_kode_fakultas'), 'fakultas', ['kode_fakultas'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_fakultas_kode_fakultas'), table_name='fakultas')
    op.drop_table('fakultas')
    # ### end Alembic commands ###
