import sqlite3

def add_student():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    id = int(input("Enter ID: "))
    name = input("Enter Name: ")
    branch = input("Enter Branch: ")
    year = int(input("Enter Year: "))
    cgpa = float(input("Enter CGPA: "))

    cursor.execute(
        "INSERT INTO students VALUES (?, ?, ?, ?, ?)",
        (id, name, branch, year, cgpa)
    )

    conn.commit()
    conn.close()

    print("Student Added Successfully!")


def view_students():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    print("\n----- Student Records -----")

    for student in students:
        print(student)

    conn.close()


def search_student():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    id = int(input("Enter Student ID: "))

    cursor.execute("SELECT * FROM students WHERE id = ?", (id,))
    student = cursor.fetchone()

    if student:
        print("\nStudent Found:")
        print(student)
    else:
        print("Student Not Found!")

    conn.close()


def update_student():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    id = int(input("Enter Student ID to Update: "))
    new_name = input("Enter New Name: ")
    new_branch = input("Enter New Branch: ")
    new_year = int(input("Enter New Year: "))
    new_cgpa = float(input("Enter New CGPA: "))

    cursor.execute(
        "UPDATE students SET name=?, branch=?, year=?, cgpa=? WHERE id=?",
        (new_name, new_branch, new_year, new_cgpa, id)
    )

    conn.commit()
    conn.close()

    print("Student Updated Successfully!")


def delete_student():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    id = int(input("Enter Student ID to Delete: "))

    cursor.execute("DELETE FROM students WHERE id = ?", (id,))

    conn.commit()
    conn.close()

    print("Student Deleted Successfully!")