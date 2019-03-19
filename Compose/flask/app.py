from flask import Flask, Response, render_template, request, url_for, redirect
from redis import Redis
import os

app = Flask(__name__)
redis = Redis(host = 'redis', port=6379)

@app.route("/flask")
def home():
    return '''
        <!DOCTYPE html>
        <html lang="en" dir="ltr">
        <head>
        <meta charset="utf-8">
        <title>Flask Parent Template</title>
        <link rel="stylesheet" href="{{ url_for('static',     filename='css/template.css') }}">
        </head>
        <body>
            <header>
            <div class="container">
                <h1 class="logo">First Flask Web App</h1>
                <strong><nav>
                <ul class="menu">
                    <li><a href="redis">Redis</a></li>
                </ul>
                </nav></strong>
            </div>
            </header>
        </body>
        </html>
    '''

@app.route("/flask/redis")
def hello():
    redis.incr('hits')
    return 'Hello from Flask! You have seen this %s times.' % redis.get('hits')

if __name__ == "__main__":
    app.run("0.0.0.0", port=8080, debug=True)