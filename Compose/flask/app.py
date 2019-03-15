from flask import Flask, Response
from redis import Redis
import os

app = Flask(__name__)
redis = Redis(host = 'redis', port=6379)


@app.route("/")
def hello():
    redis.incr('hits')
    return 'Hello from Flask! You have seen this %s times.' % redis.get('hits')

if __name__ == "__main__":
    app.run("0.0.0.0", port=8080, debug=True)