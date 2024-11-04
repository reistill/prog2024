from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

#abre a página inicial
@app.route("/")
def inicial():
    return render_template("index.html")

app.run(debug=True)

