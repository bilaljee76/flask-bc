import sqlite3

connection = sqlite3.connect(
    "students.db"
)

cursor = connection.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS students(
    
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    name TEXT,

    course TEXT

    )
    """
)

connection.commit()

connection.close()

print("Database Created Successfully")