from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash

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

@student.route(
        "/student/add",
        methods=["GET", "POST"]
        )
def add_student():

    if request.method=="POST":
        name = request.form.get("name")
        course = request.form.get("course")
        
        connection = sqlite3.connect("students.db")

        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO students
            (name, course)

            VALUES(?, ?)
            """,
            (name, course)
        )

        connection.commit()

        connection.close()

        flash(
            "Student Added Successfully!"
        )

        return redirect(
            url_for("student.students_db")
        )
    
    return render_template(
        "add_student.html"
    )

@student.route(
    "/student/update/<int:student_id>",
    methods=["GET", "POST"]
)
def update_student(student_id):

    if request.method == "POST":

        name = request.form.get("name")
        course = request.form.get("course")

        connection = sqlite3.connect(
            "students.db"
        )

        cursor = connection.cursor()

        cursor.execute(
            """
            UPDATE students

            SET
                name = ?,
                course = ?

            WHERE id = ?
            """,
            (name, course, student_id)
        )

        connection.commit()

        connection.close()

        flash(
            "Student Updated Successfully!"
        )

        return redirect(
            url_for("student.students_db")
        )

    connection = sqlite3.connect(
        "students.db"
    )

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT *
        FROM students

        WHERE id = ?
        """,
        (student_id,)
    )

    student = cursor.fetchone()

    connection.close()

    return render_template(
        "update_student.html",
        student=student
    )


@student.route(
    "/student/delete/<int:student_id>"
)
def delete_student(student_id):

    connection = sqlite3.connect(
        "students.db"
    )

    cursor = connection.cursor()

    cursor.execute(
        """
        DELETE FROM students

        WHERE id = ?
        """,
        (student_id,)
    )

    connection.commit()

    connection.close()

    flash(
            "Student Updated Successfully!"
        )

    return redirect(
        url_for("student.students_db")
    )