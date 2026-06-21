from flask import Blueprint
from flask import Flask
from flask import render_template
from flask import request

predict = Blueprint("predict",__name__)

@predict.route("/form", methods=["GET", "POST"])
def form_page():
    
    if request.method == "POST":
        
        username = request.form["username"]

        return f"Welcome {username}"
    
    return render_template("form.html")


@predict.route("/predict", methods=["GET", "POST"])
def predict_page():

    if request.method == "POST":

        try:
        
            hours = int(
                request.form.get("hours")
            )

            if hours < 0:
                return "Hours cannot be negative."
            
            marks = min(
                hours * 10,
                100
            )

            return render_template(
                "result.html",
                marks=marks
            )
    
        except ValueError:
            return "Please enter valid numbers"

    return render_template("predict.html")


@predict.route("/result")
def result_page():
    marks = 90

    return render_template(
        "result_status.html",
        marks=marks
    )