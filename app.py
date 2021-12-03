"""
Flask Application Entrypoint

Here the application is initialized with all the resources, apps and
blueprints.

You might also want create more flask instances for testing and other stuff.
"""

from flask import Flask

from blueprints import blog, user


# Flask instance
app = Flask(__name__)

# Blueprints Initialzr
blog.init_app(app)
user.init_app(app)

# Other Routes you can to the app
@app.route("/")
def index():
    return "Hello World"
