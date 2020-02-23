"""
******************************************
MAIN - Route file
******************************************
"""

import os
from flask import request, render_template, Blueprint, current_app
from myapp import mysqldb, logger


main = Blueprint('main', __name__)

# Start of Routes
@main.route('/', methods=['GET'])
def root():
    sql = f"SELECT * FROM product_categories ORDER BY id ASC"

    # logger.warning('A warning occurred (%d apples)', 42)
    logger.error('An error occurred')
    logger.info(sql)

    response = mysqldb.fetch_rows(sql)

    if response['status']:
        print(response['rows'])

    return render_template('index.html')
