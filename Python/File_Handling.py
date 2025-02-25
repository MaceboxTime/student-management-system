import pandas as pd
"""1️⃣ फाइल खोलना (Opening a File)
Python में open() फ़ंक्शन से फाइल खोली जाती है।"""
f = open("data.txt", "r")
content = f.read()
print(content)
f.close()
"""
2️⃣ फाइल लिखना (Writing to a File)
'w' (write mode) फाइल को पूरी तरह से नया बना देता है और पुराने डेटा को हटा देता है।
"""
f = open("data.txt","w")
f.write("Hello, this is a new file!\n")
f.write("File handling in Python is easy.")
f.close()
"""
3️⃣ फाइल में डेटा जोड़ना (Appending Data)
'a' (append mode) पुराने डेटा को हटाए बिना नया डेटा जोड़ता है।
"""
f = open("data.txt", "a")
f.write("\nThis is an additional line.")
f.close()
"""
4️⃣ फाइल लाइन-बाय-लाइन पढ़ना (Reading Line by Line)
✅ Example: readlines() से फाइल पढ़ना
"""
f = open("data.txt","r")
lines = f.readline()
for line in lines:
    print(line.strip())
f.close()
"""
5️⃣ With Statement (Best Practice)
with का उपयोग करने से हमें manually close() नहीं करना पड़ता।
"""
with open("data.txt","r") as f:
    content = f.read()
    print(content)
with open("data.txt","r") as f:
    lines = f.readline()
    print(F"First Line: {lines[0].strip()}")
    print(F"Second Line: {lines[2].strip()}")
f = open("data.txt","r")
print("wel")
co = f.read()
print(co)
f.close()
# df = pd.read_excel("product.xlsx")
# print(F"df")