# Citation for __init__.py:
# Date: 05/18/2022
# Copied from: OSU cs340_starter_app
# Source URL: https://github.com/mlapresta/cs340_starter_app

import os

from flask import Flask

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    from . import db
    db.init_app(app)
    
    return app
