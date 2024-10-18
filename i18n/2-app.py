#!/usr/bin/env python3

"""Import necessary modules"""
from flask import Flask, render_template, request
from flask_babel import Babel

"""
This module initializes the Flask application
and sets up the Babel instance for internationalization.
"""
babel = Babel()
app = Flask(__name__)
"""
The Flask application instance.
"""


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
    return render_template("2-index.html")


"""
Route for the root URL.
"""
app.route("/")(index)

"""
Run the app if this module is executed directly.
"""


@babel.localeselector
def get_locale():
    """
    Returns the best match for the user's locale
    based on the Accept-Language header.

    :return: The best match for the user's locale (e.g. 'en', 'fr')
    """
    return request.accept_languages.best_match(["en", "fr"])


if __name__ == "__main__":
    app.run()
