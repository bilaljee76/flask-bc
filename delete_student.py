import sqlite3

connection = sqlite3.connect(
    "students.db"
)

cursor = connection.cursor()

cursor.execute(
    """
    DELETE FROM students

    WHERE id = 2
    """
)

connection.commit()

connection.close()

print("Student Deleted Successfully")