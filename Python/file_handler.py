import csv
from student import Student
class StudentManager:
    FILE_NAME = "students.csv"

    @staticmethod
    def save_to_file(student):
        with open(StudentManager.FILE_NAME, mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["Name", "Age", "Student Class", "City"])
            if file.tell() == 0:
                writer.writeheader()
            writer.writerow(student.to_dict())

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