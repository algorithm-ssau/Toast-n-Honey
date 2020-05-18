from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_assets import Environment
from .assets import compile_assets

app = Flask(__name__, instance_relative_config=False)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/Toast-N-Honey.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

assets = Environment(app)
compile_assets(assets)
