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
    cakes = Products.query.filter(Products.typeId == 1).all()
    return render_template("cakes.html", cakes=cakes)


@app.route("/macarons/")
def macarons():
    macarons = Products.query.filter(Products.typeId == 3).all()
    return render_template("macarons.html", macarons=macarons)


@app.route("/desserts/")
def desserts():
    return render_template("desserts.html")


@app.route("/delivery/")
def delivery():
    return render_template("delivery.html")


@app.route("/details/<int:id>")
def details(id):
    product = Products.query.filter(Products.id == id).first_or_404()
    return render_template("details.html", product=product)


@app.errorhandler(404)
def product_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def product_not_found(e):
    return render_template('404.html'), 500
