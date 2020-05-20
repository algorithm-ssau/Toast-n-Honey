from flask import render_template
from TnH_app import app
from TnH_app.models import *


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
    idCakes = Products.query.filter(Products.typeId == 1).all()
    return render_template("cakes.html", filedirectory=idCakes[1].photo)


@app.route("/macarons/")
def macarons():
    return render_template("macarons.html")


@app.route("/desserts/")
def desserts():
    return render_template("desserts.html")


@app.route("/delivery/")
def delivery():
    return render_template("delivery.html")


@app.route("/details/")
def details():
    return render_template("details.html")
