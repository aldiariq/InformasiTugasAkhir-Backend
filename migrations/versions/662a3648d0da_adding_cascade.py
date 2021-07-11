"""adding cascade

Revision ID: 662a3648d0da
Revises: 54155df4c6cd
Create Date: 2021-07-10 22:51:42.443272

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '662a3648d0da'
down_revision = '54155df4c6cd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('dosen_ibfk_1', 'dosen', type_='foreignkey')
    op.drop_constraint('dosen_ibfk_2', 'dosen', type_='foreignkey')
    op.create_foreign_key(None, 'dosen', 'prodi', ['id_prodi'], ['id_prodi'], onupdate='CASCADE', ondelete='CASCADE')
    op.create_foreign_key(None, 'dosen', 'fakultas', ['id_fakultas'], ['id_fakultas'], onupdate='CASCADE', ondelete='CASCADE')
    op.drop_constraint('mahasiswa_ibfk_2', 'mahasiswa', type_='foreignkey')
    op.drop_constraint('mahasiswa_ibfk_1', 'mahasiswa', type_='foreignkey')
    op.create_foreign_key(None, 'mahasiswa', 'fakultas', ['id_fakultas'], ['id_fakultas'], onupdate='CASCADE', ondelete='CASCADE')
    op.create_foreign_key(None, 'mahasiswa', 'prodi', ['id_prodi'], ['id_prodi'], onupdate='CASCADE', ondelete='CASCADE')
    op.drop_constraint('prodi_ibfk_1', 'prodi', type_='foreignkey')
    op.create_foreign_key(None, 'prodi', 'fakultas', ['id_fakultas'], ['id_fakultas'], onupdate='CASCADE', ondelete='CASCADE')
    op.drop_constraint('tugasakhir_ibfk_4', 'tugasakhir', type_='foreignkey')
    op.drop_constraint('tugasakhir_ibfk_1', 'tugasakhir', type_='foreignkey')
    op.drop_constraint('tugasakhir_ibfk_3', 'tugasakhir', type_='foreignkey')
    op.drop_constraint('tugasakhir_ibfk_2', 'tugasakhir', type_='foreignkey')
    op.create_foreign_key(None, 'tugasakhir', 'prodi', ['id_prodi'], ['id_prodi'], onupdate='CASCADE', ondelete='CASCADE')
    op.create_foreign_key(None, 'tugasakhir', 'mahasiswa', ['id_mahasiswa'], ['id_mahasiswa'], onupdate='CASCADE', ondelete='CASCADE')
    op.create_foreign_key(None, 'tugasakhir', 'dosen', ['id_dosen'], ['id_dosen'], onupdate='CASCADE', ondelete='CASCADE')
    op.create_foreign_key(None, 'tugasakhir', 'fakultas', ['id_fakultas'], ['id_fakultas'], onupdate='CASCADE', ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'tugasakhir', type_='foreignkey')
    op.drop_constraint(None, 'tugasakhir', type_='foreignkey')
    op.drop_constraint(None, 'tugasakhir', type_='foreignkey')
    op.drop_constraint(None, 'tugasakhir', type_='foreignkey')
    op.create_foreign_key('tugasakhir_ibfk_2', 'tugasakhir', 'mahasiswa', ['id_mahasiswa'], ['id_mahasiswa'])
    op.create_foreign_key('tugasakhir_ibfk_3', 'tugasakhir', 'prodi', ['id_prodi'], ['id_prodi'])
    op.create_foreign_key('tugasakhir_ibfk_1', 'tugasakhir', 'dosen', ['id_dosen'], ['id_dosen'])
    op.create_foreign_key('tugasakhir_ibfk_4', 'tugasakhir', 'fakultas', ['id_fakultas'], ['id_fakultas'])
    op.drop_constraint(None, 'prodi', type_='foreignkey')
    op.create_foreign_key('prodi_ibfk_1', 'prodi', 'fakultas', ['id_fakultas'], ['id_fakultas'])
    op.drop_constraint(None, 'mahasiswa', type_='foreignkey')
    op.drop_constraint(None, 'mahasiswa', type_='foreignkey')
    op.create_foreign_key('mahasiswa_ibfk_1', 'mahasiswa', 'prodi', ['id_prodi'], ['id_prodi'])
    op.create_foreign_key('mahasiswa_ibfk_2', 'mahasiswa', 'fakultas', ['id_fakultas'], ['id_fakultas'])
    op.drop_constraint(None, 'dosen', type_='foreignkey')
    op.drop_constraint(None, 'dosen', type_='foreignkey')
    op.create_foreign_key('dosen_ibfk_2', 'dosen', 'fakultas', ['id_fakultas'], ['id_fakultas'])
    op.create_foreign_key('dosen_ibfk_1', 'dosen', 'prodi', ['id_prodi'], ['id_prodi'])
    # ### end Alembic commands ###
