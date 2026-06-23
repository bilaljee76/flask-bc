import sqlite3

connection = sqlite3.connect(
    "students.db"
)

cursor = connection.cursor()

cursor.execute(
    """
    INSERT INTO students
    (name, course)

    VALUES
    ('Amjad', 'HTMX')
    """
)

connection.commit()

connection.close()

print("Student Added Successfully")