#!/usr/bin/env python3
"""
shebang to create a PY script
"""


from datetime import datetime
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Union, Dict
import pytz
from pytz.exceptions import UnknownTimeZoneError

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
    current_time = datetime.now(pytz.timezone(get_timezone()))
    if get_locale() == 'en':
        g.time = current_time.strftime("%b %d, %Y, %I:%M:%S %p")
    elif get_locale() == 'fr':
        g.time = current_time.strftime("%d %b %Y à %H:%M:%S")
    else:
        g.time = current_time.strftime("%b %d, %Y, %I:%M:%S %p")


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


@babel.timezoneselector
def get_timezone():
    """method to handle timezone using babel"""
    requested_timezone = request.args.get('timezone')
    if requested_timezone:
        try:
            pytz.timezone(requested_timezone)
            return requested_timezone
        except UnknownTimeZoneError:
            return app.config['BABEL_DEFAULT_TIMEZONE']

    if g.user and 'timezone' in g.user:
        try:
            pytz.timezone(g.user['timezone'])
            return g.user['timezone']
        except UnknownTimeZoneError:
            return app.config['BABEL_DEFAULT_TIMEZONE']

    return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/')
def index() -> str:
    """index to run the home route"""
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
