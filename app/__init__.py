import os
import config
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from celery import Celery, current_app
from celery.bin import worker


app = Flask(__name__)
app.config.from_object(config.Config)
app.config.from_envvar('WOLFIT_SETTINGS')
app.config['SQLALCHEMY_DATABASE_URI'] = config.Config.DATABASE_URI(app)


celery = Celery('tasks', backend='redis://localhost', broker='redis://localhost')
application = current_app._get_current_object()
worker = worker.worker(app=app)


db = SQLAlchemy(app)
login = LoginManager(app)
migrate = Migrate(app, db)
bootstrap = Bootstrap(app)


from app import models, routes
