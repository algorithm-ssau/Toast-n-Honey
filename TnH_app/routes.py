from flask import render_template

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


@app.route("/macarons/")
def macarons():
    return render_template("macarons.html")


@app.route("/desserts/")
def desserts():
    return render_template("desserts.html")


@app.route("/delivery/")
def delivery():
    return render_template("delivery.html")
