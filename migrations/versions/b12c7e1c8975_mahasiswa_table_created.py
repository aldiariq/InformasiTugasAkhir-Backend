"""mahasiswa table created

Revision ID: b12c7e1c8975
Revises: 506f4a20dbcd
Create Date: 2021-06-27 19:25:25.259600

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b12c7e1c8975'
down_revision = '506f4a20dbcd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('mahasiswa',
    sa.Column('id_mahasiswa', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('nim_mahasiswa', sa.String(length=250), nullable=False),
    sa.Column('nama_mahasiswa', sa.String(length=250), nullable=False),
    sa.Column('angkatan_mahasiswa', sa.Integer(), nullable=False),
    sa.Column('id_prodi', sa.BigInteger(), nullable=True),
    sa.Column('reated_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['id_prodi'], ['prodi.id_prodi'], ),
    sa.PrimaryKeyConstraint('id_mahasiswa')
    )
    op.create_index(op.f('ix_mahasiswa_nim_mahasiswa'), 'mahasiswa', ['nim_mahasiswa'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_mahasiswa_nim_mahasiswa'), table_name='mahasiswa')
    op.drop_table('mahasiswa')
    # ### end Alembic commands ###