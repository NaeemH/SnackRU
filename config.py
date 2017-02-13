import os

basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = 'snackru'

SQLALCHEMY_DATABASE_URI = 'mysql://snackru:snackru@localhost/snackru'

SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

OAUTH_CREDENTIALS = {
    'snackru': {
        'id': '',
        'secret': ''
    }
}

UPLOAD_FOLDER = os.path.join(basedir, 'uploads')

LOG_FILENAME = "snackru.log"

LOG_FORMAT = ""

ALLOWED_EXTENSIONS = ["pdf"]
