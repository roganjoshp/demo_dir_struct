from flask import Flask
from flask_wtf.csrf import CSRFProtect

from roof.util import do_something

csrf = CSRFProtect()


def create_app():
    app = Flask(__name__)
    csrf.init_app(app)

    from roof.flaskapp.home import bp as core

    app.register_blueprint(core)

    return app
