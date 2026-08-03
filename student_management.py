students = []

while True:
    print("\n" + "=" * 40)
    print("      STUDENT MANAGEMENT SYSTEM")
    print("=" * 40)

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        roll = input("Enter roll number: ")
        marks = input("Enter student marks: ")

        student = {
            "name": name,
            "roll": roll,
            "marks": marks
        }

        students.append(student)
        print("\nStudent Added Successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("\nNo students found.")
        else:
            print("\nStudent List")
            print("-" * 30)
            for student in students:
                print("Name :", student["name"])
                print("Roll :", student["roll"])
                print("Marks:", student["marks"])
                print("-" * 30)

    elif choice == "3":
        roll = input("Enter roll number to search: ")

        found = False
        for student in students:
            if student["roll"] == roll:
                print("\nStudent Found")
                print("Name :", student["name"])
                print("Roll :", student["roll"])
                print("Marks:", student["marks"])
                found = True
                break

        if not found:
            print("Student not found.")

    elif choice == "4":
        roll = input("Enter roll number to update: ")

        found = False
        for student in students:
            if student["roll"] == roll:
                student["name"] = input("Enter new name: ")
                student["marks"] = input("Enter new marks: ")
                print("Student Updated Successfully!")
                found = True
                break

        if not found:
            print("Student not found.")

    elif choice == "5":
        roll = input("Enter roll number to delete: ")

        found = False
        for student in students:
            if student["roll"] == roll:
                students.remove(student)
                print("Student Deleted Successfully!")
                found = True
                break

        if not found:
            print("Student not found.")

    elif choice == "6":
        print("Thank you! Exiting program...")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 6.")