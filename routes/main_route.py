from flask import Blueprint
from flask import render_template

main = Blueprint("main", __name__)

@main.route("/")
def home_page():
    return render_template("index.html")


@main.route("/about")
def about_page():
    return render_template("about.html")


@main.route("/portfolio")
def portfolio_page():

    name = "Bilal Asghar"
    goal = "Python Developer"
    skill = "Flask + Machine Learning"

    return render_template(
        "portfolio.html",
        name=name,
        goal=goal,
        skill=skill
    )