#!/usr/bin/env python3
"""
shebang to create a PY script
"""


from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """method to define locale using babel"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


class Config:
    """class to run config to en and UTC"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

babel = Babel(app)

app.url_map.strict_slashes = False


@app.route('/')
def index() -> str:
    """index to run the home route"""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(debug=True)
