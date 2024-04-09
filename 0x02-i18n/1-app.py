#!/usr/bin/env python3
"""
shebang to create a PY script
"""


from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)


class Config:
    """class to run config to en and UTC"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAUL_TIMEZONE = "UTC"


app.config.from_object(Config)

babel = Babel(app)


@app.route('/')
def index():
    """index to run the home route"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
