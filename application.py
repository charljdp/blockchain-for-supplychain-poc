from flask import Flask

app = Flask(__name__)

@app.route("/register")
def hello_world():
    return "<p> Register a node </p>"


@app.route("/add")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/remove")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/audit")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/find")
def hello_world():
    return "<p>Hello, World!</p>"