import sqlite3

connection = sqlite3.connect(
    "students.db"
)

cursor = connection.cursor()

cursor.execute(
    """
    UPDATE students

    SET course = 'Machine Learning'

    WHERE id = 1
    """
)

connection.commit()

connection.close()

print("Student Updated Successfully")