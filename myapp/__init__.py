"""
******************************************
package init file
******************************************
"""

import logging
from flask import Flask, Blueprint
from logging.handlers import RotatingFileHandler

from myapp.config import Config
from myapp.database import Database

logger = logging.getLogger('werkzeug')
mysqldb = Database(logger)


def create_app(config_class=Config):

    app = Flask(__name__)

    app.config.from_object(config_class)

    formatter = logging.Formatter(app.config['LOG_FORMATTER'])
    log_file = f"{app.config['LOG_DIR']}/{app.config['LOG_FILENAME']}"
    handler = RotatingFileHandler(
        log_file, maxBytes=app.config['LOG_MAX_BYTES'], backupCount=app.config['LOG_BACKUP_COUNT'])
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    mysqldb.init_app(app)

    from myapp.main.routes import main
    from myapp.admin.index import admin

    app.register_blueprint(main)
    app.register_blueprint(admin, url_prefix='/admin')

    return app
