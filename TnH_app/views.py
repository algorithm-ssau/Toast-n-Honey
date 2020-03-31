from flask import Flask, render_template

from . import app


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route("/cheesecakes/")
def cheesecakes():
    return render_template("cheesecakes.html")

@app.route("/macarons/")
def cheesecakes():
    return render_template("macarons.html")