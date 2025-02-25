"""
 1️⃣ Lists (सूची)
 Mutable (बदल सकते हैं)
Ordered (क्रम में रहते हैं)
Duplicates Allow (डुप्लिकेट वैल्यू हो सकती हैं)
"""
fruits = ["Apple","Banana","Mango","Orange"]
fruits.append("Grapes")
fruits.insert(1,"Pineapple")
fruits.remove("Orange")
print(fruits)
print("Banana" in fruits)
for fruit in fruits:
    print(fruit)
"""
✅ 2️⃣ Tuples (अपरिवर्तनीय सूची)
Immutable (बदल नहीं सकते)
Ordered (क्रम में रहते हैं)
Duplicates Allow (डुप्लिकेट वैल्यू हो सकती हैं)
"""
number = (10,20,30,40)
print(number[1])
for i in number:
    print(i)
num_list = list(number)
num_list.append(50)
num_tup = tuple(num_list)
print(num_tup)
"""
 3️⃣ Dictionaries (शब्दकोश)
Key-Value Pairs (चाबी-मूल्य रूप में डेटा स्टोर करता है)
Unordered (क्रम गारंटीड नहीं होता)
Mutable (बदल सकते हैं)
"""
student = {
    "name": "Ariyan",
    "Age": 24,
    "course": "MCA",
    "skills":["Python", "SQL", "ML"]
}
print(student)
student["city"] = "Noida"
del student["Age"]
print(student.keys())
print(student.values())
for keys, value in student.items():
    print(F"{keys}: {value}")
"""
✅ 4️⃣ Sets (समूह)
Unique Elements (डुप्लिकेट नहीं होते)
Unordered (क्रम गारंटीड नहीं होता)
Mutable (बदल सकते हैं)
"""
numbers = {1,2,3,4,5}
numbers.add(6)
numbers.remove(3)
set1 = {1,2,3}
set2 = {3,5,6}
print(set1.union(set2))
print(set1.intersection(set2))