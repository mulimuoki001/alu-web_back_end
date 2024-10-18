from flask import Flask, request
from flask_babel import Babel

"""
This module initializes the Flask application
and sets up the Babel instance for internationalization.
"""

app = Flask(__name__)
"""
The Flask application instance.
"""


def get_locale():
    """
    Returns the best match for the user's locale
    based on the Accept-Language header.

    :return: The best match for the user's locale (e.g. 'en', 'fr', 'es')
    """
    return request.accept_languages.best_match(
        ["en", "fr", "es"]
    )  # add your supported languages here


babel = Babel(app, locale_selector=get_locale)
"""
The Babel instance for internationalization, initialized
with the Flask application and locale selector function.
"""
