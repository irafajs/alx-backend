#!/usr/bin/env python3
"""
shebang to create a PY script
"""


from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Union, Dict


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """class to run config to en and UTC"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


def get_user(user_id) -> Union[Dict, None]:
    """method to handle the logged user by id"""
    login_as = request.args.get('login_as')
    if login_as:
        user_id = int(login_as)
    if user_id in users:
        return users[user_id]
    else:
        return None


@app.before_request
def before_request() -> None:
    """method to get user using get_user"""
    user_id = request.args.get('login_as')
    g.user = get_user(int(user_id)) if user_id else None


@babel.localeselector
def get_locale() -> str:
    """method to define locale using babel"""
    requested_locale = request.args.get('locale')
    if requested_locale:
        return requested_locale
    if g.user and 'locale' in g.user:
        return g.user['locale']
    header_locale = request.accept_languages.best_match(
            app.config['LANGUAGES'])
    if header_locale:
        return header_locale
    return app.config['BABEL_DEFAULT_LOCALE']


@app.route('/')
def index() -> str:
    """index to run the home route"""
    return render_template('6-index.html')


if __name__ == '__main__':
    app.run(debug=True)
