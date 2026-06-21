import sqlite3

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
students = cursor.fetchall()

print(students)

connection.close()