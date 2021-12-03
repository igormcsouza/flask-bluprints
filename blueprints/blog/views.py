from flask import jsonify, request

from blueprints.blog.models import Repository


repository = Repository()


def index():
    """Blog main page."""
    return "This is a blog index page."

def get_all():
    """Return data on the database with no filter."""
    return jsonify(repository.get_all())