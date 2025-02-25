class Student:
    def __init__(self, name, age, student_class, city):
        self.name = name
        self.age = age
        self.student_class = student_class
        self.city = city

    def to_dict(self):
        return {"Name": self.name, "Age": self.age, "Student Class": self.student_class, "City": self.city}