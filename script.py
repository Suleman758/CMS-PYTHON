def enroll_course():
    courses = ['A', 'B', 'C', 'D', 'E']
    enrolled_courses = []

    print("Available Courses:")
    for i, course in enumerate(courses, 1):
        print(f"{i}. Course {course}")

    while len(enrolled_courses) < 5:
        choice = int(input("Enter the course number you want to enroll in (1-5): "))
        if 1 <= choice <= 5:
            enrolled_courses.append(courses[choice - 1])
            print(f"Enrolled in Course {courses[choice - 1]}")
        else:
            print("Invalid choice. Please select a valid course number.")

        more = input("Do you want to enroll in another course? (y/n): ")
        if more.lower() != 'y':
            break

    print("You have enrolled in the following courses:", ' '.join(enrolled_courses))


def attendance_management():
    students = int(input("Enter the number of students: "))
    attendance = {}

    for _ in range(students):
        name = input("Enter student name: ")
        status = input(f"Mark attendance for {name} (P/A): ")
        attendance[name] = "Present" if status.lower() == 'p' else "Absent"

    print("\nAttendance Record:")
    for name, status in attendance.items():
        print(f"{name} - {status}")


def fee_management():
    total_fee = 300000
    print("\nFee Management:")
    print("1. Pay Online")
    print("2. Generate Fee Challan")

    option = int(input("Choose an option (1-2): "))
    if option == 1:
        print(f"1. Single Payment - PKR {total_fee}")
        print(f"2. 3 Installments - PKR {total_fee // 3} each")
        installment = int(input("Enter your choice (1-2): "))
        if installment == 1:
            print("You selected Single Payment. Payment successful!")
        elif installment == 2:
            print("You selected 3 Installments. First payment successful!")
        else:
            print("Invalid installment choice!")
    elif option == 2:
        print("Fee Challan Generated! Print and pay at the bank.")
    else:
        print("Invalid option. Try again.")


def menu():
    while True:
        print("\nMenu Options:")
        print("1. Enroll in Course")
        print("2. Attendance Management")
        print("3. Fee Management")
        print("4. Exit")

        choice = int(input("Enter your choice (1-4): "))
        if choice == 1:
            enroll_course()
        elif choice == 2:
            attendance_management()
        elif choice == 3:
            fee_management()
        elif choice == 4:
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")


def login_page():
    correct_username = "Bnu"
    correct_password = "Bnu"

    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username == correct_username and password == correct_password:
        print("Welcome!")
        menu()
    else:
        print("Invalid username or password.")


def main():
    print("WELCOME")
    login_page()


if __name__ == "__main__":
    main()
