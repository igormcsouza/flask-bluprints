from flask import request

from blueprints.user.models import Repository
from blueprints.user.utis import decode_query_string


repository = Repository()


def index(username: str):
    """Very first route for index."""
    return f"Hello {username}"


def login():
    """Login the user, getting the user and returning the token."""
    query_string = decode_query_string(request.query_string)

    username = query_string.get('username', '')
    password = query_string.get('password', '')

    # Validate the user
    can_login, token = repository.is_valid(username, password)

    if can_login:
        return f"Welcome! You're logged! Use this token: {token}"
    
    return "Your user or password wasn't recognized."
