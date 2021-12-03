from flask import jsonify, request

from blueprints.blog.models import Repository


repository = Repository()


def index():
    return "This is a blog index page."

def get_all():
    return jsonify(repository.get_all())