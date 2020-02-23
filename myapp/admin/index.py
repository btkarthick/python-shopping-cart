"""
******************************************
ADMIN - Route file
******************************************
"""

from myapp.admin.product_routes import routes as product_routes
from flask import Blueprint

admin = Blueprint('admin', __name__)


@admin.route('/', methods=['GET'])
def home():
    return 'Admin Home'


routes = (product_routes)

for route in routes:
    admin.add_url_rule(route['rule'], endpoint=route.get(
        'endpoint', None), view_func=route['view_func'], **route.get('options', {}))
