import sqlite3

conn = sqlite3.connect("students.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY,
    name TEXT,
    branch TEXT,
    year INTEGER,
    cgpa REAL
)
""")

conn.commit()

print("Student Table Created Successfully")

conn.close()