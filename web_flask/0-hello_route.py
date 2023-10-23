#!/usr/bin/python3
<<<<<<< HEAD
"""Starts a Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'
"""
=======
"""Start Flask web application"""

>>>>>>> ff5b37980a6b5965b2af7be224cdc6de93def969
from flask import Flask

app = Flask(__name__)


<<<<<<< HEAD
@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
=======
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Routing to root, strict_slashes ensure
    the URL works when it ends both with or without the /
    """
>>>>>>> ff5b37980a6b5965b2af7be224cdc6de93def969
    return "Hello HBNB!"


if __name__ == "__main__":
<<<<<<< HEAD
    app.run(host="0.0.0.0")
=======
    app.run(host='0.0.0.0', port=5000)
>>>>>>> ff5b37980a6b5965b2af7be224cdc6de93def969
