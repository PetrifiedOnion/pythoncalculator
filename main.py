from re import template
from flask import Flask, render_template, request, flash
from matplotlib import pyplot as plt
import uuid

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "static"

@app.route("/calculator")
def index():
    return render_template("index.html")

@app.route("/calculator/make-plot")
def make_plot():

    x_values = [1, 2, 3, 4]
    y_values = [5, 4, 6, 2]

    plt.plot(x_values, y_values)
    filename = str(uuid.uuid4())
    plt.savefig("static/"+filename)
    return filename

@app.route("/calculator/<image>")
def display_plot(image):
    return render_template("index.html",plot_filename="static/%s.png" % image)
