from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from . import app

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/contacts/")
def contacts():
    return render_template("contacts.html")

@app.route("/cheesecakes/")
def cheesecakes():
    return render_template("cheesecakes.html")

@app.route("/cakes/")
def cakes():
    return render_template("cakes.html")

@app.route("/desserts/")
def desserts():
    return render_template("desserts.html")