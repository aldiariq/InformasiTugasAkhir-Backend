from app import db
from app.model.fakultas import Fakultas
from app.model.prodi import Prodi
from datetime import datetime

class Mahasiswa(db.Model):
    id_mahasiswa = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    nim_mahasiswa = db.Column(db.String(250), index=True, unique=True, nullable=False)
    nama_mahasiswa = db.Column(db.String(250), nullable=False)
    angkatan_mahasiswa = db.Column(db.Integer, nullable=False)
    id_fakultas = db.Column(db.BigInteger, db.ForeignKey(Fakultas.id_fakultas, ondelete='CASCADE', onupdate='CASCADE'))
    id_prodi = db.Column(db.BigInteger, db.ForeignKey(Prodi.id_prodi, ondelete='CASCADE', onupdate='CASCADE'))
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_at = db.Column(db.DateTime(), default=datetime.utcnow)

    def __repr__(self):
        return '<Mahasiswa {}>'.format(self.id_mahasiswa)