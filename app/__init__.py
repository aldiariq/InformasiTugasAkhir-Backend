from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

from app import routes
from app.model import admin
from app.model import fakultas
from app.model import prodi
from app.model import dosen
from app.model import mahasiswa
from app.model import tugasakhir