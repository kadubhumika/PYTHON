print("You are welcome to my Students Marks Manager!")
final_details = {}

def view_menu():
    while True:
        print("\n=== MENU ===")
        print("1. Add New Student")
        print("2. View Student Details")
        print("3. Find Average of Students")
        print("4. Remove Student Details (average < 30)")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_all_students()
        elif choice == '3':
            find_average()
        elif choice == '4':
            remove_low_average_students()
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid Choice. Please try again.")

def add_student():
    name = input("Enter student name: ")

    if name in final_details:
        print("Student already exists. Adding more subjects...")
    else:
        final_details[name] = {}

    n = int(input(f"How many subjects for {name}? "))
    for i in range(n):
        subject = input(f"  Enter subject {i + 1}: ")
        mark = int(input(f"  Enter marks for {subject}: "))
        final_details[name][subject] = mark

def view_all_students():
    if not final_details:
        print("No student data available.")
        return

    print("\n===== All Student Details =====")
    for student, subjects in final_details.items():
        print(f"\nStudent name: {student}")
        for subject, mark in subjects.items():
            print(f"  {subject}: {mark}")

def find_average():
    if not final_details:
        print("No student data available.")
        return

    for student, subjects in final_details.items():
        print(f"\nStudent name: {student}")
        for subject, mark in subjects.items():
            print(f"  {subject}: {mark}")
        avg = sum(subjects.values()) / len(subjects)
        print(f"  ➤ Average marks of {student}: {avg:.2f}")

def remove_low_average_students():
    if not final_details:
        print("No student data available.")
        return

    removed_students = []
    for student in list(final_details.keys()):
        subjects = final_details[student]
        if len(subjects) == 0:
            continue
        avg = sum(subjects.values()) / len(subjects)
        if avg < 30:
            removed_students.append(student)
            del final_details[student]

    if removed_students:
        print("Removed students with average < 30:")
        for student in removed_students:
            print(f"  - {student}")
    else:
        print("No students removed. All have average >= 30.")

# Run the menu
view_menu()
