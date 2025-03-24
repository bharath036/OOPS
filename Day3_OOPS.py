'''
📌 Concepts:
✅ Single & Multiple Inheritance
✅ Method Overriding & super()
✅ Polymorphism (Duck Typing, Method Overloading)

🎯 Tasks (Push to GitHub):
☑ Create a Vehicle class with move() method.
☑ Inherit it in Car class and override move().
☑ Implement multiple inheritance with Person and Employee.

🎯 Mini Project:
☑ E-commerce Product System - Implement Product, ElectronicItem, and ClothingItem classes with custom discount logic.

🔗 Resources:

Python Inheritance
https://realpython.com/inheritance-composition-python/

GitHub Repo: [Your Repo Link]
'''

'''
is a relationship --> Inheritance 
has a replationship --> composition or Aggregation

"""
--------------------------------------------------------------------
--------------------------------------------------------------------
🚀 IS-A vs HAS-A Relationship in Object-Oriented Programming (OOP)
====================================================================

🔹 IS-A Relationship (Inheritance)
   - When one class **inherits** from another class.
   - Uses **Inheritance** (class Child(Parent))
   - Follows a **Parent-Child** hierarchy.

🔹 HAS-A Relationship (Composition/Aggregation)
   - When one class **contains** an instance of another class.
   - Uses **Composition** (an object inside another class)
   - Follows a **Whole-Part** relationship.

====================================================================
"""

# 🟢 IS-A Relationship (Inheritance) Example
class Vehicle:
    def move(self):
        print("This vehicle moves")

# Car IS-A Vehicle (Car inherits from Vehicle)
class Car(Vehicle):  
    def wheels(self):
        print("This car has 4 wheels")

# Creating an object of Car
my_car = Car()
my_car.move()    # Inherited from Vehicle class
my_car.wheels()  # Defined in Car class

"""
🔹 Output:
This vehicle moves
This car has 4 wheels
"""

# 🟢 HAS-A Relationship (Composition) Example
class Engine:
    def start(self):
        print("Engine starts")

# Car HAS-A Engine (Car contains an Engine)
class Car:
    def __init__(self):
        self.engine = Engine()  # Creating an Engine object inside Car

    def drive(self):
        print("Car is moving...")
        self.engine.start()  # Using Engine's method

# Creating an object of Car
my_car = Car()
my_car.drive()

"""
🔹 Output:
Car is moving...
Engine starts
"""

"""
====================================================================
🛠 KEY DIFFERENCES: IS-A vs HAS-A
====================================================================
| Feature      | IS-A (Inheritance) | HAS-A (Composition) |
|-------------|------------------|------------------|
| Definition  | One class **inherits** from another | One class **contains** an instance of another class |
| Relationship Type | Parent-Child | Whole-Part |
| Example | **Car IS-A Vehicle** | **Car HAS-A Engine** |
| Flexibility | Less flexible (Tightly coupled) | More flexible (Loosely coupled) |
| Code Reusability | Inherits all parent methods | Uses only required methods |

====================================================================
"""

# 🟢 Real-Life Examples of IS-A & HAS-A

"""
🔹 IS-A Examples (Inheritance)
------------------------------
1️⃣ Dog IS-A Animal → Dog inherits from Animal.
2️⃣ Car IS-A Vehicle → Car inherits from Vehicle.
3️⃣ Apple IS-A Fruit → Apple inherits from Fruit.

🔹 HAS-A Examples (Composition)
-------------------------------
1️⃣ Car HAS-A Engine → Car contains an Engine.
2️⃣ Person HAS-A Phone → Person has a Phone object.
3️⃣ House HAS-A Door → House contains a Door object.
"""

# 🟢 Example: Real-World HAS-A Relationship
class Phone:
    def call(self):
        print("Making a phone call...")

class Person:
    def __init__(self):
        self.phone = Phone()  # Person HAS-A Phone

    def make_call(self):
        print("Person is using the phone")
        self.phone.call()  # Using the Phone object inside Person

# Creating a Person object
person = Person()
person.make_call()

"""
🔹 Output:
Person is using the phone
Making a phone call...
"""

"""
====================================================================
🎯 WHEN TO USE WHAT? (Guidelines)
====================================================================
✔ Use IS-A (Inheritance) when:
   - You need a **clear parent-child hierarchy**.
   - The subclass should inherit most behaviors from the parent.

✔ Use HAS-A (Composition) when:
   - Objects **work together** but don’t share identity.
   - You want **more flexibility** & **less dependency**.
   - Example: A Car **has** an Engine, but a Car **is not** an Engine.

====================================================================
🚀 Now You Have a Clear Understanding of IS-A & HAS-A in OOP! 🎯
====================================================================
"""
"""

************DOUBTS*************************************************

====================================================================
🚀 HAS-A Relationship: "Objects Work Together but Don't Share Identity"
====================================================================

🔹 What Does It Mean?
   - In a HAS-A relationship, **one object contains another object**, but they are still **separate** entities.
   - The contained object **belongs to** the main object but is **not the same** as it.
   - They work **together** but have **independent responsibilities**.

====================================================================
📌 Example 1: Car HAS-A Engine
====================================================================
"""

class Engine:
    def start(self):
        print("Engine is starting...")

class Car:
    def __init__(self):
        self.engine = Engine()  # Car HAS-A Engine (but they are different)

    def drive(self):
        print("Car is moving...")
        self.engine.start()  # Car uses Engine, but Car is not an Engine

# Creating a Car object
my_car = Car()
my_car.drive()

"""
🔹 Output:
Car is moving...
Engine is starting...
"""

"""
✔ The Car **contains** an Engine object.
✔ The Car **depends on** the Engine to function.
✔ The Engine and Car **work together** but **are not the same** (Car is not an Engine).
"""

"""
====================================================================
📌 Example 2: Person HAS-A Phone
====================================================================
"""

class Phone:
    def call(self):
        print("Making a phone call...")

class Person:
    def __init__(self):
        self.phone = Phone()  # Person HAS-A Phone (but they are different)

    def make_call(self):
        print("Person is using the phone")
        self.phone.call()  # Person is using the Phone, but Person is not a Phone

# Creating a Person object
person = Person()
person.make_call()

"""
🔹 Output:
Person is using the phone
Making a phone call...
"""

"""
✔ The Person **contains** a Phone object.
✔ The Phone **is used by** the Person but **is not the Person itself**.
✔ The Person and Phone **work together** but **are separate entities**.
"""

"""
====================================================================
🛠 KEY TAKEAWAYS: Why They Don't Share Identity?
====================================================================
✅ In HAS-A, one class contains another class **as an attribute**, but they remain separate.
✅ The contained object has its **own methods and responsibilities**.
✅ The containing class **uses** the object but **does not become it**.
✅ Changes to one object **don’t change the identity of the other**.

====================================================================
🎯 Real-World Examples of HAS-A (Objects Work Together but Are Separate)
====================================================================
1️⃣ A **Car HAS-A Music System** 🎶 (A Car can play music, but a Car is not a Music System)
2️⃣ A **Person HAS-A Laptop** 💻 (A Person can use a Laptop, but a Person is not a Laptop)
3️⃣ A **Company HAS-A CEO** 🏢 (A Company is led by a CEO, but a Company is not a CEO)
4️⃣ A **House HAS-A Door** 🚪 (A House has a Door, but a House is not a Door)

====================================================================
🚀 Now You Have a Clear Understanding of HAS-A & Object Independence! 🎯
====================================================================
"""

'''

#Abstract base class (ABC): We can import this from abc module

'''
abc are defined but it doesn't have implementations
from abc import ABC,abstractmethod
class Employee(ABC):
    def __init__(self, id, name):
        self.id = id
        self.name = name

    @abstractmethod
    def calculate_payroll(self):
        pass

You derive Employee from ABC, making it an abstract base class. Then, you decorate the .calculate_payroll() method with the @abstractmethod decorator.

This change has two nice side-effects:

You’re telling users of the module that objects of type Employee can’t be created.
You’re telling other developers working on the hr module that if they derive from Employee, then they must override the .calculate_payroll() abstract method.

##############################class explosion problem.??
If you’re not careful, inheritance can lead you to a huge hierarchical class structure that’s hard
to understand and maintain. This is known as the class explosion problem


Types of inheritance --> https://www.geeksforgeeks.org/types-of-inheritance-python/
'''
#Single inheritance
'''
class Parent:
    def func1(self):
        print("This is parent class")

#Derieved class 
class child(Parent):
    def func2(self):
        print("This function is child class")

object = child()
object.func2()
object.func1()

'''

#Multiple inheritance --> When a class can be derieved from more than one class, this type is known as multiple inheritance.
'''
#Base class1
class Mother:
    mothername = ""
    def mother(self):
        print(self.mothername)

#Base class2 

class Father:
    fathername = ""
    def father(self):
        print(self.fathername)

#Derieved class
class Son(Mother,Father):
    def parents(self):
        print("Father :", self.fathername)
        print("Mother :",self.mothername)

s1 = Son()
s1.fathername = "Ram"
s1.mothername = "Sita"
s1.parents()
'''

#Multilevel inheritance : features of base class and derived class are further inherited into the new derieved class. 
#Similar relationship to a child and a grandfather
'''
#Base class 
class Grandfather:
    def __init__(self,grandfathername):
        self.grandfathername = grandfathername

#Intermediate class
class Father(Grandfather):
    def __init__(self, fathername,grandfathername):
        #super().__init__(grandfathername)
        self.fathername = fathername 
        #invoking constructor of grandfather class
        Grandfather.__init__(self,grandfathername)

#Derieved class 

class Son(Father):
    def __init__(self, sonname,fathername, grandfathername):
        self.sonname = sonname
        
        #invoking constructor of Father class 
        Father.__init__(self, fathername, grandfathername)

    def print_name(self):
        print("Grandfather :", self.grandfathername)
        print('Fathername :', self.fathername)
        print("Sonname :", self.sonname)

s1 = Son('Prince','Rampal','Lal mani')
print(s1.fathername)
s1.print_name()
'''
#Hierarchical inheritance:
#When more than one derived class are created from a single base this
# type of inheritance is called hierarchical inheritance. In this program, 
# we have a parent (base) class and two child (derived) classes.

#Hybrid inheritance 
#Inheritance consisting of multiple types of inheritance is called hybrid inheritance.

'''
class School:
	def func1(self):
		print("This function is in school.")


class Student1(School):
	def func2(self):
		print("This function is in student 1. ")


class Student2(School):
	def func3(self):
		print("This function is in student 2.")


class Student3(Student1, School):
	def func4(self):
		print("This function is in student 3.")


# Driver's code
object = Student3()
object.func1()
object.func2()

'''

#Python super()
'''
In python., super() is used to refer the parent class or superclass.It allows us to call
methods defined in the superclass from sub class to extend and customize the functionality 
inherited from parent class.

A method from parent class can be called in python using super() function. It's typical practice
in oops to call the methods from super class and enable method overidding and inheritance.
'''

'''
class Emp:
    def __init__(self,id,name,Add):
        self.id = id 
        self.name = name 
        self.Add = Add 

#class freelace inherits EMP
class Freelance(Emp):
    def __init__(self, id, name, Add, Email):
        super().__init__(id, name, Add)
        self.Email = Email

#creating object 
Emp1 = Freelance(103,'Suraj','Noida','kk@gmail.com')
print("The id is:", Emp1.id)
print("The name is", Emp1.name)

Difference between super() and super 
super(): This is the function call that returns a proxy object to the superclass,
allowing you to call its methods.
super: This is the actual built-in function or type itself. Without the parentheses 
and subsequent method call, it’s just a reference to the function and does nothing on its own.
'''

#Method overriding
'''
Method overriding is the ability that allows a subclass to provide specific implementation
of a method that is already provided by one of its super-classes.
'''
'''
# Python program to demonstrate 
# calling the parent's class method 
# inside the overridden method 
class Parent(): 
    
    def show(self): 
        print("Inside Parent") 
        
class Child(Parent): 
    
    def show(self): 
        
        # Calling the parent's class 
        # method 
        Parent.show(self) 
        print("Inside Child") 
        
# Driver's code 
obj = Child() 
obj.show() 

'''
#Using super keyword
'''
# Python program to demonstrate 
# calling the parent's class method 
# inside the overridden method using 
# super() 
class Parent(): 
    
    def show(self): 
        print("Inside Parent") 
        
class Child(Parent): 
    
    def show(self): 
        
        # Calling the parent's class 
        # method 
        super().show() 
        print("Inside Child") 
        
# Driver's code 
obj = Child() 
obj.show() 
'''
'''
# Program to define the use of super() 
# function in multiple inheritance 
class GFG1: 
    def __init__(self): 
        print('HEY !!!!!! GfG I am initialised(Class GEG1)') 
    
    def sub_GFG(self, b): 
        print('Printing from class GFG1:', b) 
    
# class GFG2 inherits the GFG1 
class GFG2(GFG1): 
    def __init__(self): 
        print('HEY !!!!!! GfG I am initialised(Class GEG2)') 
        super().__init__() 
    
    def sub_GFG(self, b): 
        print('Printing from class GFG2:', b) 
        super().sub_GFG(b + 1) 
    
# class GFG3 inherits the GFG1 ang GFG2 both 
class GFG3(GFG2): 
    def __init__(self): 
        print('HEY !!!!!! GfG I am initialised(Class GEG3)') 
        super().__init__() 
    
    def sub_GFG(self, b): 
        print('Printing from class GFG3:', b) 
        super().sub_GFG(b + 1) 
    
    
# main function 
if __name__ == '__main__': 
    
    # created the object gfg 
    gfg = GFG3() 
    
    # calling the function sub_GFG3() from class GHG3 
    # which inherits both GFG1 and GFG2 classes 
    gfg.sub_GFG(10) 

'''

#Polymorphism
'''
#Duck typing
#dynamic typing
print(len("Hello"))  # String length
print(len([1, 2, 3]))  # List length

print(max(1, 3, 2))  # Maximum of integers
print(max("a", "z", "m"))  # Maximum in strings


#Operator overloading
means giving extended meaning beyond their predefined operational meaning
 + is used to add 2 integers as well as join 2 strings and merge two lists

Suppose if we want to add two objects using '+' ., it throws an error
as compiler don't know how to add 2 objects. for this we define a method for
an operator and that process is called operator overloading

To perform operator overloading, python provides some special functions or magic 
functions that is automatically called when it is associated with that particular 
operator.
Ex: when we use + operator, the magic method __add__ is automatically invoked in which
the operation for + operator is defined.

Ex:--WSee the below example
'''

'''
class A:
    def __init__(self,a):
        self.a = a 

    #adding two objects
    def __add__(self, o):
        return self.a + o.a 
    
obj1 = A(1)
obj2 = A(2)
obj3 = A('Geeks')
obj4 = A('For')

print(obj1+obj2)
print(obj3+obj4)

print(obj1.__add__(obj2))

https://www.geeksforgeeks.org/operator-overloading-in-python/
'''

#Polymorphism
'''
Polymorphism allows methods in different classes to share the same
name but perform distinct tasks.
'''

'''
class Shape:
    def area(self):
        return "undefined"

class Rectangle(Shape):
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def area(self):
        return self.a*self.b 
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius 

    def area(self):
        return 3.14*self.radius*self.radius 
    
shapes = [Rectangle(1,2), Circle(4)]
for shape in shapes:
    print(shape.area())

'''

#Types of Polymorphism
'''
1.Compile-time Polymorphism
2.Runtime Polymorphism

Duck Typing: If it acts like a duck, it’s a duck! Python doesn’t check the type, just the behavior.

Dynamic Typing: A variable can hold anything and can change its type as needed. Python figures it out on the fly.

'''

#Tasks    

'''
🎯 Tasks (Push to GitHub):
☑ Create a Vehicle class with move() method.
☑ Inherit it in Car class and override move().
☑ Implement multiple inheritance with Person and Employee.
'''

class Vehicle:
    def move(self):
        print("Parent class move method")

class Car(Vehicle):
    def move(self):
        return f"Car class move method"

obj1 = Car()
print(obj1.move())

class Person:
    def fun(self):
        return f"Person class"
    
class Employee:
    def fun1(self):
        return f"Employee class"

class Child(Person,Employee):
    def fun2(self):
        print("Child class")

object1 = Child()
print(object1.fun())