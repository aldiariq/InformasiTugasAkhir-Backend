from app import db
from app.model.mahasiswa import Mahasiswa
from app.model.dosen import Dosen
from app.model.fakultas import Fakultas
from app.model.prodi import Prodi
from datetime import datetime

class Tugasakhir(db.Model):
    id_tugasakhir = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    judul_tugasakhir = db.Column(db.String(250), index=True, unique=True, nullable=False)
    tanggal_tugasakhir = db.Column(db.Date, nullable=False)
    status_tugasakhir = db.Column(db.Enum("SELESAI", "BELUMSELESAI"), nullable=False)
    id_mahasiswa = db.Column(db.BigInteger, db.ForeignKey(Mahasiswa.id_mahasiswa, ondelete='CASCADE', onupdate='CASCADE'))
    id_dosen = db.Column(db.BigInteger, db.ForeignKey(Dosen.id_dosen, ondelete='CASCADE', onupdate='CASCADE'))
    id_fakultas = db.Column(db.BigInteger, db.ForeignKey(Fakultas.id_fakultas, ondelete='CASCADE', onupdate='CASCADE'))
    id_prodi = db.Column(db.BigInteger, db.ForeignKey(Prodi.id_prodi, ondelete='CASCADE', onupdate='CASCADE'))
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_at = db.Column(db.DateTime(), default=datetime.utcnow)

    def __repr__(self):
        return '<Tugasakhir {}>'.format(self.id_tugasakhir)