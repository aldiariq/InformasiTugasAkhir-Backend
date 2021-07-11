"""created dosen table

Revision ID: 506f4a20dbcd
Revises: 361de8390c60
Create Date: 2021-06-27 19:07:02.372728

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '506f4a20dbcd'
down_revision = '361de8390c60'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dosen',
    sa.Column('id_dosen', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('nip_dosen', sa.String(length=250), nullable=False),
    sa.Column('nama_dosen', sa.String(length=250), nullable=False),
    sa.Column('id_prodi', sa.BigInteger(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['id_prodi'], ['prodi.id_prodi'], ),
    sa.PrimaryKeyConstraint('id_dosen')
    )
    op.create_index(op.f('ix_dosen_nip_dosen'), 'dosen', ['nip_dosen'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_dosen_nip_dosen'), table_name='dosen')
    op.drop_table('dosen')
    # ### end Alembic commands ###
