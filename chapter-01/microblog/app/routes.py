from flask import render_template
from app import app


@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Miguel"}
    posts = [
        {"author": {"username": "John"}, "body": "Beautiful day in Portland!"},
        {"author": {"username": "Susan"}, "body": "The Avengers movie was so cool!"},
    ]
    return render_template("index.html", user=user, posts = posts)


@app.route("/about")
def about():
    return "About Page"


@app.route("/contact")
def contact():
    return "Contact us"
