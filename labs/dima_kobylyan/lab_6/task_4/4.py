from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/11.09.11.09")
def new_funk():
    return "<p>Привет   Малая!</P"
