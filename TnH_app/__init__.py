from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__, instance_relative_config=False)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/Toast-N-Honey.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
