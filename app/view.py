from app import app
from flask import render_template


@app.route("/")
def Hello():
    name = "Vasa"
    return render_template("index.html", n=name)
