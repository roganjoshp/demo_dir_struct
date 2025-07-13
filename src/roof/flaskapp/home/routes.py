from flask import render_template

from roof.flaskapp.home import bp
from roof.util import do_something


@bp.route("/", methods=["GET"])
def home():
    do_something()
    return render_template("home/homepage.html")
