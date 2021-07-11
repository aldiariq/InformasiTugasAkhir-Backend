import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DATABASE_HOST = str(os.environ.get("DATABASE_HOST"))
    DATABASE_USERNAME = str(os.environ.get("DATABASE_USERNAME"))
    DATABASE_PASSWORD = str(os.environ.get("DATABASE_PASSWORD"))
    DATABASE_NAME = str(os.environ.get("DATABASE_NAME"))

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + DATABASE_USERNAME + ':' + DATABASE_PASSWORD + '@' + DATABASE_HOST + '/' + DATABASE_NAME
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    JSON_SORT_KEYS = False
    JWT_SECRET = str(os.environ.get("JWT_SECRET"))
    JWT_SECRET_KEY = "HS256"

    UPLOAD_FOLDER = str(os.environ.get("UPLOAD_FOLDER"))
    MAX_UPLOAD_SIZE = 3 * 1024 * 1024