from flask import Flask
from flask import render_template
import random

app = Flask(__name__)

@app.route("/")
def hello_world():
    message  = "Computational Spatial Humanities Course"
    return render_template("leipzig.html", message=message)

@app.route("/test.html")
def hello_other_world():
    return "<p>Hello, other o world!</p>"


@app.route("/data.geojson")
def geodata():
    return "{}"

app.run(debug=True)