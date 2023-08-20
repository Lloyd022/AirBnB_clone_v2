#!/usr/bin/python3
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello World!'
"""
from flask import Flask, render_templete

app = Flask("__name__")


@app.route("/", strict_slashes=False)
def hello():
    """Return 'Hello World!'"""
    return render_templete("10-hbnb_filters.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=none)
