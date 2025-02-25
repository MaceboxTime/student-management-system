import csv

class Student:
    def __init__(self, student_id, name, age, student_class):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.student_class = student_class

    def to_dict(self):
        return {
            "Student ID": self.student_id,
            "Name": self.name,
            "Age": self.age,
            "Class": self.student_class
        }

class StudentManager:
    FILE_NAME = "students_new.csv"

    @staticmethod
    def save_to_file(student):
        with open(StudentManager.FILE_NAME, mode="a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["Student ID", "Name", "Age", "Class"])
            if file.tell() == 0:
                writer.writeheader()
            writer.writerow(student.to_dict())

    @staticmethod
    def load_students():
        students = []
        try:
            with open(StudentManager.FILE_NAME, mode="r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    students.append(Student(row["Student ID"], row["Name"], row["Age"], row["Class"]))
        except FileNotFoundError:
            pass
        return students

    @staticmethod
    def load_from_file():
        students = []
        try:
            with open(StudentManager.FILE_NAME, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    students.append(row)
        except FileNotFoundError:
            pass
        return students
    @staticmethod
    def update_student(student_id, new_name, new_age, new_class):
        students = StudentManager.load_students()
        updated = False
        with open(StudentManager.FILE_NAME, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["Student ID", "Name", "Age", "Class"])
            writer.writeheader()
            for student in students:
                if student.student_id == student_id:
                    student.name = new_name
                    student.age = new_age
                    student.student_class = new_class
                    updated = True
                writer.writerow(student.to_dict())
        return updated

    @staticmethod
    def delete_student(student_id):
        students = StudentManager.load_students()
        students = [student for student in students if student.student_id != student_id]

        with open(StudentManager.FILE_NAME, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["Student ID", "Name", "Age", "Class"])
            writer.writeheader()
            for student in students:
                writer.writerow(student.to_dict())

        return True

class StudentOperations:
    @staticmethod
    def add_student():
        student_id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        age = input("Enter Student Age: ")
        student_class = input("Enter Student Class: ")
        student = Student(student_id, name, age, student_class)
        StudentManager.save_to_file(student)
        print("✅ Student added successfully!")

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
    def update_student():
        student_id = input("Enter Student ID to Update: ")
        new_name = input("Enter New Name: ")
        new_age = input("Enter New Age: ")
        new_class = input("Enter New Class: ")
        if StudentManager.update_student(student_id, new_name, new_age, new_class):
            print("✅ Student updated successfully!")
        else:
            print("⚠ Student ID not found!")

    @staticmethod
    def delete_student():
        student_id = input("Enter Student ID to Delete: ")
        StudentManager.delete_student(student_id)
        print("✅ Student deleted successfully!")

def menu():
    while True:
        print("\n📌 Student Management System 📌")
        print("1️⃣ Add Student")
        print("2️⃣ Update Student")
        print("3️⃣ Delete Student")
        print("4️⃣ View Students")
        print("5️⃣ Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            StudentOperations.add_student()
        elif choice == "2":
            StudentOperations.update_student()
        elif choice == "3":
            StudentOperations.delete_student()
        elif choice == "4":
            StudentOperations.view_students()
        elif choice == "5":
            print("🚀 Exiting the system...")
            break
        else:
            print("⚠ Invalid choice! Try again.")

if __name__ == "__main__":
    menu()