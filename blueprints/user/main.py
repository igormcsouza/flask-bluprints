from flask import Blueprint
from flask.app import Flask

from blueprints.user import views


bp = Blueprint(name="User", url_prefix="/user", import_name=__name__)

bp.add_url_rule("/<string:username>", view_func=views.index)
bp.add_url_rule("/login", view_func=views.login)


def init_app(app: Flask):
    app.register_blueprint(bp)
