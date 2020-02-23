"""
******************************************
Configuration class file
******************************************
"""

import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Set Flask configuration vars."""

    # General Config
    TESTING = os.getenv('TESTING')
    DEBUG = os.getenv('DEBUG')
    SECRET_KEY = os.getenv('SECRET_KEY')

    # DB Config
    MYSQL_HOST = os.getenv('MYSQL_HOST')
    MYSQL_USER = os.getenv('MYSQL_USER')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
    MYSQL_DB_NAME = os.getenv('MYSQL_DB_NAME')

    # Logger Config
    LOG_FORMATTER = os.getenv('LOG_FORMATTER')
    LOG_DIR = os.getenv('LOG_DIR')
    LOG_FILENAME = os.getenv('LOG_FILENAME')
    LOG_MAX_BYTES = int(os.getenv('LOG_MAX_BYTES'))
    LOG_BACKUP_COUNT = os.getenv('LOG_BACKUP_COUNT')


class DevConfig(Config):
    DEBUG = True


class ProdConfig(Config):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = ''
