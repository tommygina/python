#!/usr/bin/python3
# -*- coding:utf-8 -*-

import time

import redis
from flask import Flask

app = Flask(__name__)
# cache = redis.Redis(host="192.168.99.100", port=6379)
# cache = redis.Redis(host="192.168.200.128", port=6379)
cache = redis.Redis(host="127.0.0.1", port=6379)

def get_count():
    retries = 5
    while True:
        try:
            return cache.incr("hits")
        except redis.exceptions.ConnectionError as exec:
            if retries == 0:
                raise exec
            retries -= 1
            time.sleep(0.3)

@app.route("/message")
def message():
    return "<h1>hello message</h1>"
    pass

@app.route("/helloflask")
def test():
    return "hello flask, and i love you!"
    pass


@app.route("/")
def hello():
    cnt = get_count()
    return "hello world! cnt={}\n".format(cnt)

def main():
    print("hello docker")
    app.run(host="127.0.0.1", port="5000", debug=True)
    # app.run(host="127.0.0.1", port="5000", debug=True)
    pass

# 主函数
if __name__ == "__main__":
    main()