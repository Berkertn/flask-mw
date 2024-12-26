import os
from urllib.parse import urlparse


class Config:
    """Base configuration."""
    DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://username:password@localhost:5432/my_database')
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    parsed_uri = urlparse(DATABASE_URL)
    DB_NAME = parsed_uri.path[1:]
    DB_USER = parsed_uri.username
    DB_PASSWORD = parsed_uri.password
    DB_HOST = parsed_uri.hostname
    DB_PORT = parsed_uri.port or 5432


class DevelopmentConfig(Config):
    """Development-specific configuration."""
    DEBUG = True
    DATABASE_URL = os.getenv('DEV_DATABASE_URL', 'postgresql://postgres:postgres@localhost:5433/commencis_ai')
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    parsed_uri = urlparse(DATABASE_URL)
    DB_NAME = parsed_uri.path[1:]
    DB_USER = parsed_uri.username
    DB_PASSWORD = parsed_uri.password
    DB_HOST = parsed_uri.hostname
    DB_PORT = parsed_uri.port or 5433


class ProductionConfig(Config):
    """Production-specific configuration."""
    DEBUG = False
    DATABASE_URL = os.getenv('PROD_DATABASE_URL', 'postgresql://prod_user:prod_password@192.168.1.100:5432/prod_db')
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    parsed_uri = urlparse(DATABASE_URL)
    DB_NAME = parsed_uri.path[1:]
    DB_USER = parsed_uri.username
    DB_PASSWORD = parsed_uri.password
    DB_HOST = parsed_uri.hostname
    DB_PORT = parsed_uri.port or 5432
