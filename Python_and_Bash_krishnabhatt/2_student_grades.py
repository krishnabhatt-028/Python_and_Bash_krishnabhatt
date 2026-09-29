# Task 2: Student Grades
# A dictionary stores student names (keys) and their grades (values).

students = {
    "Amit": "A",
    "Neha": "B",
}

while True:
    print("\n--- Student Grades Menu ---")
    print("1. Add a new student and grade")
    print("2. Update an existing student's grade")
    print("3. Print all student grades")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        name = input("Enter student name: ")
        if name in students:
            print(name, "already exists. Use option 2 to update the grade.")
        else:
            grade = input("Enter grade: ")
            students[name] = grade
            print(name, "added with grade", grade)

    elif choice == "2":
        name = input("Enter student name: ")
        if name in students:
            grade = input("Enter new grade: ")
            students[name] = grade
            print("Updated", name, "to grade", grade)
        else:
            print(name, "not found. Use option 1 to add the student.")

    elif choice == "3":
        if len(students) == 0:
            print("No students yet.")
        else:
            print("\nStudent Grades:")
            for name, grade in students.items():
                print(name, "->", grade)

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, 3 or 4.")
