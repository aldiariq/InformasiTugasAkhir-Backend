from app import db
from app.model.fakultas import Fakultas
from datetime import datetime

class Prodi(db.Model):
    id_prodi = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    kode_prodi = db.Column(db.String(250), index=True, unique=True, nullable=False)
    nama_prodi = db.Column(db.String(250), nullable=False)
    id_fakultas = db.Column(db.BigInteger, db.ForeignKey(Fakultas.id_fakultas, ondelete='CASCADE', onupdate='CASCADE'))
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_at = db.Column(db.DateTime(), default=datetime.utcnow)

    def __repr__(self):
        return '<Prodi {}>'.format(self.id_prodi)