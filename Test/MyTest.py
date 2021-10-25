#!/usr/bin/python3

import time
import sys
import json
import redis

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
	return "<h1>hello flask</h1>"
	pass

def main():
	print("hello python")
	app.run(host="127.0.0.1", port="8888")

if __name__ == "__main__":
	main()