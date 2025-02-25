from pygame.sndarray import make_sound


class Car:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price
    def show_details(self):
        return F"Car: {self.brand} {self.model}, Price: {self.price}"

car1 = Car("Toyota","Camry",45)
car2 = Car("BMW","X5",90)
print(car1.show_details())
print(car2.show_details())
"""q 2Inheritance """
class Animal:
    def __init__(self,name,sound):
        self.name = name
        self.sound = sound
    def make_sound(self):
        print(F"{self.name} says {self.sound}")
class Dog(Animal):
    def __init__(self,name):
        super().__init__(name, "Bark")
class Cat(Animal):
    def __init__(self,name):
        super().__init__(name,"Meow")
dog = Dog("Bruno")
cat = Cat("Whiskers")
dog.make_sound()
cat.make_sound()
"""q 3Polymorphism """
import math
class Shape:
    def area(self):
        pass
class  Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius * self.radius
class Rectangle(Shape):
    def __init__(self,length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
circle = Circle(9)
rectangle = Rectangle(4,6)
print(F"Circle Area:", circle.area())
print(F"Rectangle Area: {rectangle.area()}")
"""Inheritance """
class Vehicle:
    def __init__(self,brand):
        self.brand = brand
    def show_brand(self):
        print(F"brand: {self.brand}")
class Car(Vehicle):
    def __init__(self,brand,model):
        super().__init__(brand)
        self.model = model
    def show_details(self):
        print(F"Car: {self.brand} {self.model}")

car1 = Car("Tesla", "Model S")
car1.show_brand()
car1.show_details()
"""Polymorphism """
class Dog:
    def sound(self):
        return "Bark"
class Cat:
    def sound(self):
        return "Meow"
def make_sound(animal):
    print(animal.sound())

dog = Dog()
cat = Cat()
make_sound(dog)
make_sound(cat)
"""Encapsulation """
class BanlAccount:
    def __init__(self,balance):
        self.__balance = balance
    def deposit(self,amount):
        self.__balance += amount
    def get_balance(self):
        return self.__balance
account = BanlAccount(1000)
am = int(input("enter deposit amount :"))
account.deposit(am)
print(account.get_balance())