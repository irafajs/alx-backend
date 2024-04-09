#!/usr/bin/env python3
"""
Shebang to create a PY script
"""


from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    """method index to run the home route"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)

