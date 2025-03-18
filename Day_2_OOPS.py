'''
📌 Concepts:
✅ Instance methods (self)
✅ Class methods (@classmethod)
✅ Static methods (@staticmethod)
✅ Difference between self & cls

🎯 Tasks (Push to GitHub):
☑ Create a BankAccount class with:

deposit() and withdraw() instance methods.

A @classmethod to update global interest_rate.

A @staticmethod to validate account numbers.

🎯 Mini Project:
☑ Employee Payroll System - Use class methods to apply salary increment.

🔗 Resources:

Python Class Methods Guide

GitHub Repo: [Your Repo Link]
'''

'''
DECORATOR:
Decorator is esentially a function which takes another function as argument
and returns new function with improved functionality
This allows us to use this decorators in scenarios such as logging, authentication
,memorization, allowing us to add additional functionality to existing functions or methods 
in a clean and reusable way
'''
'''
#A simple decorator function
def decorator(func):

    def wrapper():
        print("Before calling the function")
        func()
        print("After calling the function")
    
    return wrapper 

#Applying decorator to a function

@decorator
def greet():
    print("Hello, World")
greet()
'''

'''
OUTPUT:
Before calling the function
Hello, World
After calling the function
'''

#Here above @decorator syntax is a shortand for greet = decorator(greet)

#Higher order functions
'''
The functions that take one or more functions as arguments
return as a result or do both.
'''
#A higher-order function that takes another function as a argument
'''
def fun(f,x):
    return f(x)

#A simple function to pass 
def square(x):
    return x*x 

res = fun(square,5)
print(res)
'''

'''
This function fun takes two parameters:
f: A function
x: A value (number)
Inside the function, we call f(x), which means we execute the function f by passing x to it.

We can pass any function instead of square 
def cube(x):
    return x * x * x

print(fun(cube, 3))  # Output: 27

# Higher-order function that applies multiple functions in sequence
def fun(f1, f2, x):
    return f2(f1(x))  # First apply f1, then apply f2 to the result

# Function to double a number
def double(x):
    return x * 2

# Function to add 10 to a number
def add_ten(x):
    return x + 10

# Calling fun with both functions and an input number
res = fun(double, add_ten, 5)
print(res)


#We can pass list of functions as well

# Higher-order function that applies a list of functions in sequence
def apply_functions(funcs, x):
    for f in funcs:
        x = f(x)  # Apply each function one by one
    return x

# Functions
def square(x): return x * x
def double(x): return x * 2
def add_five(x): return x + 5

# List of functions
functions = [square, double, add_five]

# Call apply_functions with multiple functions
result = apply_functions(functions, 2)
print(result)

Higher-order means functions that work with other functions (as input or output).
You can pass multiple functions and apply them in order.
Using lists of functions allows for more flexibility.

'''
#Learn about closure functions??

'''
First-class function is a concept where functions are treated as first-class citizens.
By treating functions as first-class citizens, Python allows you to write more abstract,
reusable, and modular code. This means that functions in such languages are treated like any 
other variable. They can be passed as arguments to other functions, returned as values from other 
functions, assigned to variables and stored in data structures.
'''

#Types of Decorators
#1.Function decorations --> we had seen above 

#2.Method decorators
'''
Used to decorate methods within a class. They often handle special cases, such as the self
argument for instance methods.
'''
'''
def method_decorator(func):
    def wrapper(self, *args,**kwargs):
        print("Before method execution")
        res = func(self, *args,**kwargs)
        print("After method execution")
        return res 
    return wrapper

class Myclass:
    @method_decorator
    def say_hello(self):
        print("Hello!")

obj = Myclass()
obj.say_hello()
'''

#3.Class Decorators
'''
class decorators are used to modify or enhance the behaviour of class.
Like function decorators .., class decorators are applied to the class
definition.

They work by taking class as an argument and returning the modified version of class 

'''
'''
def fun(cls):
    cls.class_name = cls.__name__
    return cls 

@fun 
class Person:
    pass 

print(Person.class_name)
print("Hi")
'''

'''
Python provides several built-in decorators that are commonly used in class definitions.
These decorators modify the behaviour of methods and attributes in a class.
Most frequently used built-in decorators : @staticmethod , @classmethod, @property 
'''

#Static method

'''
If we keep static method keyword to a method in class.., without creating instance(object) we can access it using variable

There can be some functionality that relates to the class, but does not require any instance(s) to do some work, 
static methods can be used in such cases. A static method is a method which is bound to the class and not the object of 
the class. It can't access or modify class state. It is present in a class because it makes sense for the method to be present 
in class. A static method does not receive an implicit first argument.

The @staticmethod decorator in Python is used to define a method inside a class that does not depend on
the instance (self) or class (cls). It behaves like a normal function, but it is part of the class for 
organizational purposes.

Both below codes works but without static method the below code cannot be
overidden in subclasses

Without @staticmethod: Works, but is unclear and not best practice.
With @staticmethod: Clearly communicates intent and avoids confusion
'''

'''
class Maths:
    
    def addNum(num1,num2):
        return num1+num2
    

res = Maths.addNum(1,2)
print(res)

# Python program to 
# demonstrate static methods 

class Maths(): 
	
	@staticmethod
	def addNum(num1, num2): 
		return num1 + num2 
		
# Driver's code 
if __name__ == "__main__": 
	
	# Calling method of class 
	# without creating instance 
	res = Maths.addNum(1, 2) 
	print("The result is", res) 
'''

# Python program to 
# demonstrate static methods 
'''
class Person: 
	def __init__(self, name, age): 
		self.name = name 
		self.age = age 
		
	# a static method to check if a Person is adult or not. 
	@staticmethod
	def isAdult(age): 
		return age > 18
		
# Driver's code 
if __name__ == "__main__": 
	res = Person.isAdult(12) 
	print('Is person adult:', res) 
	
	res = Person.isAdult(22) 
	print('\nIs person adult:', res) 
'''


'''
Use @staticmethod when:

A method does not use instance (self) or class (cls) attributes.
The method belongs to the class logically but does not need instance-specific data.
You need a utility function inside a class.
'''

'''
"""
===============================
📌 Difference: Instance Method vs. Static Method
===============================

🔹 1️⃣ Instance Method (`self`) → Instance-Specific
   - Requires `self` (instance reference)
   - Can access/modify instance variables
   - Must be called using an instance

🔹 2️⃣ Static Method (`@staticmethod`) → NOT Instance-Specific
   - Does NOT require `self`
   - Can be called using the class name
   - Used for utility functions inside a class

===============================
💡 Example 1: Instance Method (Uses `self`)
===============================
"""

class Maths:
    def addNum(self, num1, num2):  # Requires 'self'
        return num1 + num2

maths_obj = Maths()  # Create an instance
res = maths_obj.addNum(1, 2)  # Must call via instance
print("Instance Method Result:", res)  # Output: 3

# ❌ This will give an error:
# Maths.addNum(1, 2)  # TypeError: addNum() missing 1 required positional argument: 'self'

"""
===============================
💡 Example 2: Static Method (No `self`)
===============================
"""

class Maths:
    @staticmethod
    def addNum(num1, num2):  # No 'self' required
        return num1 + num2

# ✅ Can be called directly using class name
res = Maths.addNum(1, 2)
print("Static Method Result:", res)  # Output: 3

"""
===============================
🔹 When to Use What?
===============================

✅ Use **Instance Method** when:
   - The method needs to access instance variables (`self`).
   - You want to modify object-specific data.

✅ Use **Static Method** when:
   - The method is independent of instance variables.
   - It acts as a helper function inside the class.
"""

'''

#class method
'''
The classmethod() is an inbuilt function in Python, which returns
a class method for a given function. This means that classmethod() 
is a built-in Python function that transforms a regular method into 
a class method. When a method is defined using the @classmethod decorator 
(which internally calls classmethod()), the method is bound to the class 
and not to an instance of the class. As a result, the method receives the
class (cls) as its first argument, rather than an instance (self).
'''
'''
class Geeks:
    course = 'DSA'
    list_of_instances = []

    def __init__(self,name):
        self.name = name 
        Geeks.list_of_instances.append(self)

    @classmethod
    def get_course(cls):
        return f"Course:{cls.course}"
    
    @classmethod
    def get_instance_count(cls):
        return f"Number of instances: {len(cls.list_of_instances)}"
    
    @staticmethod
    def welcome_message():
        return "Welcome to Geeks for Geeks!"
    
#Creating instances
g1 = Geeks('Alicee')
g2 = Geeks('Bob')

#calling class methods
print(Geeks.get_course())
print(Geeks.get_instance_count())

#calling static method
print(Geeks.welcome_message())'
'''

'''
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_string(cls, date_string):
        year, month, day = map(int, date_string.split('-'))
        return cls(year, month, day)

date = Date.from_string('2023-07-16')
print(date.year, date.month, date.day)  
'''

'''
🎯 Tasks (Push to GitHub):
☑ Create a BankAccount class with:

deposit() and withdraw() instance methods.

A @classmethod to update global interest_rate.

A @staticmethod to validate account numbers.

🎯 Mini Project:
☑ Employee Payroll System - Use class methods to apply salary increment.
'''
'''
# Why do we use self.balance instead of just balance?
#
# The 'self' keyword refers to the specific instance of the class.
# 
# When we write 'self.balance', we are creating or accessing the instance variable 
# that belongs to that particular BankAccount object.
#
# If we use just 'balance' without 'self', it is treated as a local variable 
# inside the method or constructor. It will not be stored within the object and 
# won't persist after the method ends.
#
# Using 'self.balance' ensures that each object maintains its own separate balance 
# and the data stays tied to that specific instance.
#
# Example:
# acc1 = BankAccount(1000) → acc1.balance = 1000
# acc2 = BankAccount(2000) → acc2.balance = 2000
# Both objects have independent balances because of 'self.balance'.

I passed balance as argument in get_balance will be error.., see it
'''
'''
class BankAccount:
    def __init__(self,balance):
        self.balance = balance

    def get_balance(self):
        return f"balance is : {self.balance}"

    def deposit(self,add):
        self.balance = self.balance + add 

    def withdraw(self, sub):
        self.balance = self.balance - sub 

obj1 = BankAccount(1000)
print(obj1.get_balance()) 
print()
print(obj1.deposit(100))
print(obj1.get_balance())
'''

'''
A @classmethod to update global interest_rate.

A @staticmethod to validate account numbers.
'''
'''
#A @classmethod to update global interest_rate.
class BankAccount:
    interest_rate = 1.04
    def __init__(self,balance):
        self.balance = balance

    def get_balance(self):
        return f"balance is : {self.balance}"

    def deposit(self,add):
        self.balance = self.balance + add 

    def withdraw(self, sub):
        self.balance = self.balance - sub

#    @classmethod
#    def modify_balance(cls,balance):
#        balance = cls.interest_rate*balance 
    
    @classmethod
    def update_interest_rate(cls, new_rate):
        cls.interest_rate = new_rate

obj1 = BankAccount(1000)
print(obj1.get_balance()) 
print()
print(obj1.deposit(100))
print(obj1.get_balance())
#print(obj1.modify_balance())
print(obj1.get_balance())

#As we can see below without creating instances we modified class variables
print(f"Default Interest Rate: {BankAccount.interest_rate}")

# Update interest rate for all accounts
BankAccount.update_interest_rate(1.05)

print(f"Updated Interest Rate: {BankAccount.interest_rate}")

'''

'''
#A @staticmethod to validate account numbers.

class BankAccount:
    interest_rate = 1.04
    def __init__(self,balance):
        self.balance = balance

    def get_balance(self):
        return f"balance is : {self.balance}"

    def deposit(self,add):
        self.balance = self.balance + add 

    def withdraw(self, sub):
        self.balance = self.balance - sub

#    @classmethod
#    def modify_balance(cls,balance):
#        balance = cls.interest_rate*balance 
    
    @classmethod
    def update_interest_rate(cls, new_rate):
        cls.interest_rate = new_rate

    @staticmethod
    def validate_account_number(acc_num):
        if acc_num % 2 == 0:
            return True
        else:
            return False 

obj1 = BankAccount(1000)
print(obj1.get_balance()) 
print()
print(obj1.deposit(100)) #It gives None as we are not returning anything
print(obj1.get_balance())
#print(obj1.modify_balance())
print(obj1.get_balance())

#As we can see below without creating instances we modified class variables
print(f"Default Interest Rate: {BankAccount.interest_rate}")

# Update interest rate for all accounts
BankAccount.update_interest_rate(1.05)

print(f"Updated Interest Rate: {BankAccount.interest_rate}")

print(BankAccount.validate_account_number(1224))

'''







'''
🎯 Mini Project:
☑ Employee Payroll System - Use class methods to apply salary increment.
'''



