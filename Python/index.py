from operations import StudentOperations
def menu():
    while True:
        print("\n📚 Student Management System")
        print("1️⃣ Add Student")
        print("2️⃣ View Students")
        print("3️⃣ Search Student")
        print("4️⃣ Exit")

        choice = input("\nEnter your choice: ")
        if choice == "1":
            StudentOperations.add_student()
        elif choice == "2":
            StudentOperations.view_students()
        elif choice == "3":
            StudentOperations.search_student()
        elif choice == "4":
            print("\n🚀 Exiting... Thank you!\n")
            break
        else:
            print("\n❌ Invalid choice! Try again.\n")
menu()
