from flask import Flask, render_template, request, redirect, url_for
from pony.orm import *

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

app.run(debug=True)