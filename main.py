from re import template
from flask import Flask, render_template, request, flash

app = Flask(__name__)

@app.route("/calculator")
def index():
    return render_template("index.html")

@app.route("/<username>")
def nick_msg(username):
    return "<p>Hi %s</p>" % username