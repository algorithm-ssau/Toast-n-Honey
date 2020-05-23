from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_assets import Environment
from flask_compress import Compress
from .assets import compile_assets

app = Flask(__name__, instance_relative_config=False)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/Toast-N-Honey.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


assets = Environment(app)
compile_assets(assets)

COMPRESS_MIMETYPES = ['text/html', 'text/css', 'text/js',
                      'application/json', 'application/javascript',
                      'font/woff', 'font/ttf', 'font/otf']
COMPRESS_LEVEL = 6
COMPRESS_MIN_SIZE = 500

Compress(app)
