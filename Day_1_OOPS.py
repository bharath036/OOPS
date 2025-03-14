#Classes and objects in python
'''
class Student:
    pass
#pass is a keyword used in python to do nothing 

print(type(Student))
object_1= Student()
print(type(object_1))
#object_1 is a instance of class., a variable

#To know whether particular variable is instance of class or not, then checks and returns true or false
a = isinstance(object_1, Student)
print(a)

object_2 = {}
a=isinstance(object_2,Student)
print(a)
'''

'''
OUTPUT:
<class 'type'>
<class '__main__.Student'>
True
False
'''

'''
Special methods in python
__init__: is a special method in python that takes one argument
For that argument we can pass anything but generally self is passed 
self: is argument passed as first argument
'''

'''
class student:
    def __init__(self):
        print("initialize called!")

#Object is created
S1 = student()
print(S1)
print(type(S1))
print(student)
print(type(student))
'''

#if we print object , it gives the memory address it got stored
#if we wont give any argument it executes type error which means 1 argument is required and generally we pass self as argument.
#Using self is a standard practice , in place of self we can any argument
'''
output:-
<__main__.student object at 0x000001B1D4974A10>
<class '__main__.student'>
<class '__main__.student'>
<class 'type'>
'''


'''

#Passing arguments for initialization

class student:
    def __init__(self,name):
        self.name = name
        self.mail= name + "."+"@xyz.com"

#creating instance of a class
#s1=student()
#here we get's type error it is because we have pass 1 argument name
s1=student("john")
print(s1)
 #if we print s1, it gives memory location where it got stored
'''

'''
#defining additional methods in classes
class student:
    def __init__(self,first,last):
        self.first = first
        self.last = last
        self.mail = first + "." + last + "@xyz.com" 

    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    
s1 = student("john","michael")
print(s1.fullname())
s2 = student("abc","defg")
print(s2.mail)

#if we want delete an object we use del keyword
#del s2
#print(s2)

'''


#Introducing class variables

#class variables : The variables which are associated with the class itself and not with the particular instance of class
#instance variables: associated with an instance of a class and not with the class itself
#class variables share same memory location. If we update/modify class variables, it reflects to all objects.
#If we make changes to instance variables, it wont reflect to other objects


#Getters  and setters for private variables

#In C++, we use access specifiers(private,public,protected)., only a set of users can access it
#Instance and class variables are public by default., can be accessed from outside the class

#We can make variables private in this way
'''
class Dog:
    def __init__(self,name,breed):
        self.__name = name          #to make this variables private we use __
        self.__breed = breed

    def print_details(self):
        print("My name is %s and I am a %s" %(self.__name,self.__breed))

d1 = Dog('tom',"Golden Retriver")
d1.print_details()  #we can call function and print it but modify it as variables are private

d1.__name = "Oba"
d1.print_details()  #if we modify and print name , old name is printed and name cannot be modified with new name

#They were not really private. They was a hack we can modify it by using single under score followed by class name
d1._Dog__name = "Gen"
d1.print_details()
'''

'''
#It is not a good practice to update instance variables outside the class except by using specific functions getters

class Dog:
    def __init__(self,name,breed):
        self.__name = name
        self.__breed = breed
    
    def print_details(self):
        print("My name is %s and I am a %s" %(self.__name,self.__breed))
    
    def change_name(self,name):
        self.__name = name
    
    def change_breed(self,breed):
        self.__breed = breed 
    
d1 = Dog('Nemo','Husky')
d1.print_details()

d1.change_name('Oba')
d1.print_details()
'''

'''
#Example of using getters and setters

class Dog:
    __Species="Canine"
    def __init__(self,name,breed):
        self.__name = name
        self.__breed = breed
        self.__tricks = []

    def get_name(self):
        return self.__name 
    
    def set_name(self, name):
        self.__name = name

    def get_breed(self):
        return self.__breed
    
    def set_breed(self,breed):
        self.__breed=breed

    def add_tricks(self,tricks):
        self.__tricks.append(tricks)

    def print_details(self):
        print("My name is %s and I am a %s and I can do tricks! %s" %(self.__name,self.__breed,self.__tricks))

d1 = Dog("Tom", "Husky")
d1.print_details()

'''

'''
Class = Template / Blueprint:-->
A class is like a blueprint or template that defines attributes (data) and methods (functions) but doesn't store actual values.

Instance (Object) = Copy of Class with Its Own Data-->
When you create an object (instance) from a class, Python copies the structure (attributes & methods) into a separate entity (the instance).
Each instance gets its own copy of the data, but it can use the same methods from the class.

Ex--> 
class Car:
    def __init__(self, brand, model):
        self.brand = brand  # Attribute
        self.model = model  # Attribute

    def display_info(self):  # Method
        return f"Car: {self.brand} {self.model}"

# Creating two instances (objects)
car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")

# Each instance has its own copy of data
print(car1.display_info())  # Output: Car: Toyota Camry
print(car2.display_info())  # Output: Car: Honda Civic

# Modifying an instance's attribute
car1.brand = "Ford"
print(car1.display_info())  # Output: Car: Ford Camry


Class is a template → Defines what attributes & methods objects will have.
✅ Each object gets its own copy of attributes but shares methods from the class.
✅ Modifying one object does not affect others, as they have separate copies of data.

🔹 Think of a class like a form 📝: Each person (object) fills in their own details, but the form structure remains the same.

class variables, instance variables --> instance variables or attributes or properties can have different data
class variables data is same for all classes

Below we defined two objects from Dog class..,and returns false because they both are stored in 2 different memory locations
we can check by adding print statement and returns false
>>> a = Dog()
>>> b = Dog()
>>> a == b
False


The Dog class’s .__init__() method has three parameters, so why are
you only passing two arguments to it in the example?

When you instantiate the Dog class, Python creates a new instance of Dog and 
passes it to the first parameter of .__init__(). This essentially removes the
self parameter, so you only need to worry about the name and age parameters.

*********We wont pass self while creating instances(objects) of class

Methods like .__init__() and .__str__() are called dunder methods because they 
begin and end with double underscores. There are many dunder methods that you
can use to customize classes in Python. 

*******************************When Should You Use .__repr__() vs .__str__() in Python?
***********************https://realpython.com/python-class-constructor/ --> refer this for internal object creation understanding
'''
'''
Tasks:-->
☑ Create a Car class with brand, model, year attributes.
☑ Instantiate multiple objects and print their details.
☑ Modify an object's attribute dynamically.
☑ Build a User Management System class.
'''
#Task1--> Create a Car class with brand, model, year attributes.
#Tak2--->  Instantiate multiple objects and print their details.
'''
class Car:
    def __init__(self,brand,model,year):
        self.brand = brand 
        self.model = model 
        self.year = year 

    def print_details(self):
        return f"The brand is {self.brand} and model is {self.model} and manufactured in {self.year}"
    
car_1 = Car("Suzuki","Ciaz",2018)
print(car_1)
print(car_1.print_details())

car_2 = Car("Hyundai","Venue",2022)
print(car_2.print_details())

#Task3: Modify an object's attribute dynamically.

car_2.model = "Creta"
print(car_2.print_details())
'''
#Tak4 : Build a User Management System class.
'''
Task 4: User Management System
The User Management System should:

Create users with name, email, and age attributes.
Store multiple users and allow listing all users.
Allow updating user information dynamically.

'''
class User:
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def update_email(self, email):
        self.email = email

    def update_age(self, new_age):
        self.age = new_age

    def display_info(self):
        return f"User: {self.name}, Email: {self.email}, Age: {self.age}"

# Creating user instances
user_1 = User("John Doe", "john@example.com", 28)
user_2 = User("Alice Smith", "alice@example.com", 24)

# Printing user details
print(user_1.display_info())
print(user_2.display_info())

# Updating user details dynamically
user_1.update_email("john@newmail.com")
user_1.update_age(29)

print("After updating user details:")
print(user_1.display_info())























































