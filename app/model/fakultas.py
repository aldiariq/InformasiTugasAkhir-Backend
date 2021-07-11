from app import db
from datetime import datetime

class Fakultas(db.Model):
    id_fakultas = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    kode_fakultas = db.Column(db.String(250), index=True, unique=True, nullable=False)
    nama_fakultas = db.Column(db.String(250), nullable=False)
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_at = db.Column(db.DateTime(), default=datetime.utcnow)

    def __repr__(self):
        return '<Fakultas {}>'.format(self.kode_fakultas)