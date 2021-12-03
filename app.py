from flask import Flask

from blueprints import blog, user

app = Flask(__name__)

# Blueprints Initialz
blog.init_app(app)
user.init_app(app)

# Other Routes
@app.route("/")
def index():
    return "Hello World"
