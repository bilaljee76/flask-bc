from flask import Blueprint
from flask import render_template
from flask import request
import sqlite3
student = Blueprint("student", __name__)

@student.route("/student", methods=["GET", "POST"])
def student_page():
    
    if request.method == "POST":
        
        username = request.form.get("username")
        student_class = request.form.get("student_class")

        return render_template(
            "student_result.html",
            username=username,
            student_class=student_class
        )
    
    return render_template("student.html")
@student.route("/students")
def students_page():

    students = [
        "Bilal",
        "Ali",
        "Ahmed",
        "Ayesha",
        "Fatima"
    ]

    return render_template(
        "students.html",
        students=students
    )


@student.route("/students-db")
def students_db():
    connection = sqlite3.connect(
        "students.db"
    )

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT *
        FROM students
        """
    )

    students_records = cursor.fetchall()

    connection.close()

    return render_template(
        "students_db.html",
        students_records=students_records
    )