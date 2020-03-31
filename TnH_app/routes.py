from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from . import app

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route("/cheesecakes/")
def cheesecakes():
    return render_template("cheesecakes.html")

@app.route("/cakes/")
def cakes():
    return render_template("cakes.html")