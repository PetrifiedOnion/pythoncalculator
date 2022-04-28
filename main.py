from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Burger King!</p>"

@app.route("/<username>")
def nick_msg(username):
    return "<p>Hi %s</p>" % username