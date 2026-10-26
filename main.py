students = []


def add_student():
    student_id = input("Enter student ID: ")

    for student in students:
        if student["id"] == student_id:
            print("Error: Student ID already exists!")
            return

    name = input("Enter student name: ")

    if not name.strip():
        print("Error: Student name cannot be empty!")
        return

    try:
        marks = float(input("Enter student marks (0-100): "))

        if marks < 0 or marks > 100:
            print("Error: Marks must be between 0 and 100!")
            return

    except ValueError:
        print("Error: Please enter valid numeric marks!")
        return

    student = {
        "id": student_id,
        "name": name,
        "marks": marks
    }

    students.append(student)
    print("Student added successfully!")


def view_students():
    if not students:
        print("No students found.")
        return

    print("\n===== STUDENT RECORDS =====")

    for student in students:
        print("--------------------")
        print("Student ID:", student["id"])
        print("Student Name:", student["name"])
        print("Student Marks:", student["marks"])


def search_student():
    search_id = input("Enter student ID to search: ")

    for student in students:
        if student["id"] == search_id:
            print("\nStudent Found!")
            print("Student ID:", student["id"])
            print("Student Name:", student["name"])
            print("Student Marks:", student["marks"])
            return

    print("Student not found.")


def update_student():
    update_id = input("Enter student ID to update: ")

    for student in students:
        if student["id"] == update_id:
            print("\nCurrent Name:", student["name"])
            print("Current Marks:", student["marks"])

            new_name = input(
                "Enter new name (press Enter to keep current name): "
            )

            if new_name.strip():
                student["name"] = new_name

            new_marks = input(
                "Enter new marks (press Enter to keep current marks): "
            )

            if new_marks.strip():
                try:
                    marks = float(new_marks)

                    if marks < 0 or marks > 100:
                        print("Error: Marks must be between 0 and 100!")
                        return

                    student["marks"] = marks

                except ValueError:
                    print("Error: Please enter valid numeric marks!")
                    return

            print("Student updated successfully!")
            return

    print("Student not found.")


def delete_student():
    delete_id = input("Enter student ID to delete: ")

    for student in students:
        if student["id"] == delete_id:
            students.remove(student)
            print("Student deleted successfully!")
            return

    print("Student not found.")


def main():
    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            print("Thank you for using the Student Management System!")
            break

        else:
            print("Invalid choice! Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()