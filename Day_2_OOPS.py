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
#Learn about closure functions

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

def fun(cls):
    cls.class_name = cls.__name__
    return cls 

@fun 
class Person:
    pass 

print(Person.class_name)
print("Hi")

'''
Python provides several built-in decorators that are commonly used in class definitions.
These decorators modify the behaviour of methods and attributes in a class.
Most frequently used built-in decorators : @staticmethod , @classmethod, @property 
'''
