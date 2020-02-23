"""
******************************************
ADMIN - Product Route file
******************************************
"""

from flask import render_template, url_for

""" Routes variable declartion """
routes = []


def product_index():
    return "Product Index"


routes.append(dict(rule='/products', view_func=product_index,
                   options=dict(methods=['GET'])))
