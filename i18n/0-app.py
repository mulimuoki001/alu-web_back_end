#!/usr/bin/venv python3
from flask import Flask, render_template
from flask_babel import Babel

babel = Babel()


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_objects(Config)
babel.init_app(app)


@app.route("/")
def index():
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run()
