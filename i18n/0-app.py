#!/usr/bin/env python3

"""
This module sets up a Flask app with internationalization support using Flask-Babel.
"""

from flask import Flask, render_template
from flask_babel import Babel

"""
Instantiate the Babel object to enable
internationalization support.
"""
babel = Babel()


class Config:
    """
    Configuration class for the Flask app.

    Attributes:
        LANGUAGES (list): List of available languages.
        BABEL_DEFAULT_LOCALE (str): Default locale.
        BABEL_DEFAULT_TIMEZONE (str): Default timezone.
    """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


"""
Create a Flask app and configure it with the Config class.
"""
app = Flask(__name__)
app.config.from_object(Config)
babel.init_app(app)


def index():
    """
    Render the index.html template.

    Returns:
        str: Rendered HTML template.
    """
    return render_template("0-index.html")


"""
Route for the root URL.
"""
app.route("/")(index)

"""
Run the app if this module is executed directly.
"""
if __name__ == "__main__":
    app.run()
