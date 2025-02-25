from student import Student
from file_handler import StudentManager
class StudentOperations:
    @staticmethod
    def add_student():
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        student_class = input("Enter Class: ")
        city = input("Enter City: ")
        student = Student(name, age, student_class, city)
        StudentManager.save_to_file(student)
        print("\n✅ Student added successfully!\n")
    @staticmethod
    def view_students():
        students = StudentManager.load_from_file()
        if not students:
            print("\n❌ No students found!\n")
            return
        print("\n📌 Student List:\n")
        for student in students:
            print(student)
        print()
    @staticmethod
    def search_student():
        search_name = input("Enter Student Name to Search: ")
        students = StudentManager.load_from_file()
        found_students = [s for s in students if s["Name"].lower() == search_name.lower()]
        if found_students:
            print("\n🔎 Found Student(s):\n", found_students)
        else:
            print("\n❌ No student found with that name!\n")