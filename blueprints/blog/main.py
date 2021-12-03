from flask import Blueprint
from flask.app import Flask

from blueprints.blog import views


bp = Blueprint(name="Blog", url_prefix="/blog", import_name=__name__)

bp.add_url_rule("/", view_func=views.index)
bp.add_url_rule("/posts", view_func=views.get_all)


def init_app(app: Flask):
    app.register_blueprint(bp)
