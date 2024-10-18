#!/usr/bin/env python3

"""Import necessary modules"""
from flask import Flask, request
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


@babel.localeselector
def get_locale():
    """
    Returns the best match for the user's locale
    based on the Accept-Language header.

    :return: The best match for the user's locale (e.g. 'en', 'fr')
    """
    return request.accept_languages.best_match(["en", "fr"])
