from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class Admin(db.Model):
    id_admin = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    username_admin = db.Column(db.String(250), index=True, unique=True, nullable=False)
    password_admin = db.Column(db.String(250), nullable=False)
    nama_admin = db.Column(db.String(250), nullable=False)
    foto_admin = db.Column(db.String(250), nullable=False)
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_at = db.Column(db.DateTime(), default=datetime.utcnow)
    
    def __repr__(self):
        return '<Admin {}>'.format(self.username_admin)

    def setPassword(self, password):
        self.password_admin = generate_password_hash(password)

    def checkPassword(self, password):
        return check_password_hash(self.password_admin, password)