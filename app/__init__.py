import logging
from logging.handlers import RotatingFileHandler

from flask import Flask
from app.config import DevelopmentConfig
from app.controllers.api import api
from app.exceptions.error_handler import register_error_handlers
from app.extensions import db, migrate
from app.utils.db_utils import ensure_database_exists


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    app.config['RESTPLUS_VALIDATE'] = True  # activate the validations

    # Extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Check DB and tables
    with app.app_context():
        ensure_database_exists(app.config)
        db.create_all()

    # Register blueprints and app to flask
    api.init_app(app)
    register_error_handlers(app)

    return app


"""    # Logger
    file_handler = RotatingFileHandler("app.log", maxBytes=100000, backupCount=3)
    file_handler.setLevel(logging.WARNING)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    app.logger.addHandler(file_handler)"""
