'''
Day-4: Encapsulation and Abstraction
📌 Concepts:
✅ Public, Protected, Private Attributes
✅ Getters & Setters (@property)
✅ Abstract Classes & Methods (ABC module)

🎯 Tasks (Push to GitHub):
☑ Create a Student class with private _marks.
☑ Implement getters & setters for _marks.
☑ Implement an abstract class Shape with calculate_area() method, inherited by Circle and Rectangle.

🎯 Mini Project:
☑ Secure Login System - Implement encapsulation for handling user authentication securely.

🔗 Resources:

Encapsulation in Python

GitHub Repo: [Your Repo Link]

'''

#Access specifiers
#Public members --> can be accessed and modified from anywhere from inside or outside the class
#2.Protected members --> This are identified with _ . These are meant to be accessed only within the class or its subclass
'''
"""
📌 PROTECTED MEMBERS IN PYTHON

1. Protected members are identified with a single underscore (_) prefix.
   Example: self._age

2. Python does NOT enforce protection. It is just a naming convention to signal:
   - Internal use only (within the class or subclass).
   - Accessing them directly is technically allowed but discouraged.

3. Python follows the philosophy: "We are all consenting adults here."
   - It trusts developers to use protected members responsibly.

4. Protected members can be accessed directly from outside the class,
   but it is a bad practice as it violates the intent of the protection.
   
💡 If stricter protection is needed, use private members with a double underscore (__).

Protected Attribute (_age): This attribute is prefixed with a single underscore, 
which by convention, suggests that it should be treated as a protected member. 
It’s not enforced by Python but indicates that it should not be accessed outside of this class and its subclasses.
"""

'''
'''
class Protected:
    def __init__(self):
        self._age = 30  #Protected attribute

class Subclass(Protected):
    def display_age(self):
        print(self._age)

obj = Subclass()
obj.display_age()
print(obj._age)'
'''

#3.Private members : they are identified by __ --> double underscore.
'''
cannot be accessed directly from outside the class.
'''
'''
class Private:
    def __init__(self):
        self.__salary = 5000

    def salaty(self):
        return self.__salary #Access through private method
    
obj = Private()
print(obj.salaty()) #Works 
print(obj.__salary()) #Raises attribute error

'''

#Abstraction

'''
Hiding the implementation , irrelevant details from the user
and show the details that are relevant to the users
It hides the complex implemantation details while exposing only essential
information and functionalities to users.
Abstact classes --> we can achieve abstraction by creation abstract classes
concrete method  --> with complete implementations

'''
#Difference between Encapsulation vs Abstraction
'''
"""
📌 ABSTRACTION vs ENCAPSULATION

🔑 ABSTRACTION:
1. Hides the complex implementation details and shows only essential features.
2. Achieved using abstract classes and interfaces.
3. Focuses on *what* an object does rather than *how* it does it.
4. Example: A car's "drive" function - You know how to drive, but not how the engine works.

🔒 ENCAPSULATION:
1. Wraps data (variables) and methods (functions) into a single unit (class).
2. Protects the data from unauthorized access by restricting direct access.
3. Achieved using private and protected access modifiers.
4. Example: A car's speedometer is encapsulated; you can't change the speed directly.

🌟 KEY DIFFERENCE:
- Abstraction focuses on *hiding complexity* by showing relevant data.
- Encapsulation focuses on *protecting data* by controlling access.

📝 REMEMBER:
- Abstraction is about *design* (hiding the complex logic).
- Encapsulation is about *implementation* (hiding the internal state).
"""
'''
'''
"""
📌 ABSTRACTION vs ENCAPSULATION

🔑 ABSTRACTION:
1. Hides the complex implementation details and shows only essential features.
2. Achieved using abstract classes and interfaces.
3. Focuses on *what* an object does rather than *how* it does it.
4. Real-Life Example: Driving a car (You know how to drive, but not how the engine works).
5. Code Example:

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

c = Circle(5)
print("Area of circle:", c.area())  # Output: Area of circle: 78.5

🔒 ENCAPSULATION:
1. Wraps data (variables) and methods (functions) into a single unit (class).
2. Protects the data from unauthorized access by restricting direct access.
3. Achieved using private (__) and protected (_) access modifiers.
4. Real-Life Example: Car speedometer (You can see the speed but can't change it directly).
5. Code Example:

class Student:
    def __init__(self, name, age):
        self._name = name       # Protected member
        self.__age = age        # Private member

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid age")

s = Student("John", 20)
print("Name:", s._name)        # Accessing protected attribute (not recommended)
print("Age:", s.get_age())     # Accessing private attribute through a getter
s.set_age(25)                  # Updating age through a setter
print("Updated Age:", s.get_age())

🌟 KEY DIFFERENCE:
- Abstraction focuses on *hiding complexity* by showing relevant data.
- Encapsulation focuses on *protecting data* by controlling access.

📝 REMEMBER:
- Abstraction is about *design* (hiding the complex logic).
- Encapsulation is about *implementation* (hiding the internal state).
"""

'''
#Getters and setters
'''
Getter and Setter are methods used to access and update the 
attributes of a class.
Getter method is used to retrieve the value of private attribute
Setter is used to modify or set the value of private attribute
'''
'''
class Geek: 
    def __init__(self, age = 0): 
        self.__age = age 
    
    # getter method 
    def get_age(self): 
        return self.__age 
    
    # setter method 
    def set_age(self, x): 
        self.__age = x 

raj = Geek() 

# setting the age using setter 
raj.set_age(21) 

# retrieving age using getter 
print(raj.get_age()) 

print(raj.__age)  #__ for private and directly can't be accessed which throws error
#print(raj._age)  #if the attribute is protected we can access it

'''

'''
🎯 Tasks (Push to GitHub):
☑ Create a Student class with private _marks.
☑ Implement getters & setters for _marks.
☑ Implement an abstract class Shape with calculate_area() method, inherited by Circle and Rectangle.
'''

class Student:
    def __init__(self,marks):
        self.__marks = marks 

    def set_marks(self,marks1):
        self.__marks = marks1
    
    def get_marks(self):
        return self.__marks 
    
obj1 = Student(40)
print(obj1.get_marks())
#print(obj1.__marks)  #Throws error due to private
obj1.set_marks(40)
print(obj1.get_marks())

from abc import ABC

class Shape(ABC):
    def calculate_area(self):
        pass 

#To make it more meaningful use this __init__ constructors for
#initializing radius for circle and sides for rectangle
class Circle(Shape):
    #def __init__(self,radius):
     #   self.radius = radius

    def calculate_area(self,radius):
        return 3.14*radius*radius

class Rectangle(Shape):
    def calculate_area(self,a,b):
        return a*b
     
c1 = Circle()
print(c1.calculate_area(10))

r1 = Rectangle()
print(r1.calculate_area(2,3))