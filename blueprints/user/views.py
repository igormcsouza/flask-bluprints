from flask import request

from blueprints.user.models import Repository
from blueprints.user.utis import decode_query_string


repository = Repository()

def index(username: str):
    return f"Hello {username}"

def login():
    query_string = decode_query_string(request.query_string)

    username = query_string.get('username', '')
    password = query_string.get('password', '')

    can_login, token = repository.is_valid(username, password)

    if can_login:
        return f"Welcome! You're logged! Use this token: {token}"
    
    return "Your user or password wasn't recognized."
