from re import template
from flask import Flask, render_template, request, flash
import matplotlib.pyplot  as plt
import numpy as np
import uuid
import math as m

# fig, ax = plt.subplots()
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "static"

@app.route('/')
@app.route("/calculator", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
     
        
        datax = request.form['x_input']
        datay = request.form['y_input']

        datax_ints = []
        datay_ints = []
        for i in datax.split(','):
            datax_ints.append(int(i))
        for i in datay.split(','):
            datay_ints.append(int(i))




       
        # todo modify data so it can go into plot function below

        plt.plot(datax_ints, datay_ints)
        filename = str(uuid.uuid4())
        plt.savefig("static/plots/"+filename)
        return render_template("index.html",plot_filename="../static/plots/%s.png" % filename)

    else:
        return render_template("index.html", plot_filename="../static/default.jpg")


        
    # fig.clear(True)
        # return render_template("index.html", plot_filename="../static/default.jpg")

# @app.route("/calculator/make-plot")
# def make_plot():
#     return "test"
#     # return filename

# @app.route("/calculator/<image>")
# def display_plot(image):