#Dunder methods(magic methods) and operator overloading

'''
📌 Concepts:
✅ __str__, __repr__, __len__, __eq__, __add__
✅ Operator Overloading (+, -, *, /)

🎯 Tasks (Push to GitHub):
☑ Implement __str__ & __repr__ in Book class.
☑ Implement + operator overloading in Vector class.

🎯 Mini Project:
☑ Custom Fraction Class - Implement operator overloading for +, -, *, /.

🔗 Resources:

Magic Methods in Python

GitHub Repo: [Your Repo Link]
'''

'''
"""
📌 DUNDER METHODS (MAGIC METHODS)

🔑 What are Dunder Methods?
- Dunder methods (Double UNDERscore) are special methods with double underscores at the start and end.
- They enable built-in behaviors for objects and define how they interact with Python syntax.
- Commonly known as "magic methods" because they enable the use of operators and built-in functions.

📝 Commonly Used Dunder Methods:
1. __init__(self)  -> Constructor method
2. __str__(self)   -> Returns a human-readable string representation
3. __repr__(self)  -> Returns an official string representation
4. __len__(self)   -> Returns the length of the object
5. __getitem__(self, key) -> Access item using indexing
6. __setitem__(self, key, value) -> Assign value using indexing
7. __delitem__(self, key) -> Delete an item using indexing
8. __call__(self)  -> Makes an instance callable like a function
9. __iter__(self)  -> Returns an iterator

🔍 Example:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(Name: {self.name}, Age: {self.age})"

    def __repr__(self):
        return f"Person('{self.name}', {self.age})"

p = Person("Alice", 30)
print(str(p))    # Output: Person(Name: Alice, Age: 30)
print(repr(p))   # Output: Person('Alice', 30)

=========================================================

📌 OPERATOR OVERLOADING

🔑 What is Operator Overloading?
- Operator overloading allows the same operator to have different meanings based on the operands.
- Implemented using dunder methods that define the behavior of operators for objects.

📝 Common Operator Overloading Methods:
1. __add__(self, other)    -> Addition (+)
2. __sub__(self, other)    -> Subtraction (-)
3. __mul__(self, other)    -> Multiplication (*)
4. __truediv__(self, other) -> Division (/)
5. __floordiv__(self, other) -> Floor Division (//)
6. __mod__(self, other)    -> Modulus (%)
7. __pow__(self, other)    -> Power (**)
8. __eq__(self, other)     -> Equal (==)
9. __ne__(self, other)     -> Not Equal (!=)
10. __lt__(self, other)    -> Less Than (<)
11. __le__(self, other)    -> Less Than or Equal (<=)
12. __gt__(self, other)    -> Greater Than (>)
13. __ge__(self, other)    -> Greater Than or Equal (>=)

🔍 Example:
class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __str__(self):
        return f"{self.real} + {self.imag}i"

c1 = ComplexNumber(3, 4)
c2 = ComplexNumber(1, 2)
c3 = c1 + c2  # Uses __add__()
print(c3)  # Output: 4 + 6i

=========================================================

🌟 KEY TAKEAWAYS:
1. Dunder methods make objects behave like built-in types.
2. Operator overloading enables objects to work with operators (+, -, *, etc.).
3. Always implement __str__() and __repr__() for meaningful object representation.
4. Use operator overloading to make custom classes intuitive and easy to use.
5. Be cautious with overloading to maintain code readability and usability.

🎯 QUICK TIPS:
- Use __init__() for initialization.
- Use __str__() for a readable string representation.
- Use __add__(), __sub__(), etc., to overload arithmetic operators.
- Avoid excessive overloading to maintain clarity.
"""

'''
'''
"""
📌 __str__ vs __repr__ in Python

🔑 What is __str__?
1. Purpose: Provides a readable and human-friendly representation of an object.
2. Used when: 
   - Printing the object using print().
   - Converting the object to a string using str().
3. Goal: Make the output *easy to understand* for end users.
4. Syntax: def __str__(self): return "Readable String"

🔑 What is __repr__?
1. Purpose: Provides an unambiguous and developer-friendly representation of an object.
2. Used when:
   - Printing the object directly in the console.
   - Using repr() function.
3. Goal: Provide an output that is *precise and useful for debugging*.
4. Syntax: def __repr__(self): return "Formal Representation"

💡 Key Differences:
1. __str__ is meant for end-user readability, while __repr__ is for developers.
2. __repr__ is called when you simply type the object name in the console.
3. If __str__ is not defined, Python uses __repr__ as a fallback.

🔍 Example:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(Name: {self.name}, Age: {self.age})"  # User-friendly

    def __repr__(self):
        return f"Person('{self.name}', {self.age})"  # Debug-friendly

p = Person("Alice", 30)

# Using print() -> Calls __str__()
print(p)  # Output: Person(Name: Alice, Age: 30)

# Using repr() -> Calls __repr__()
print(repr(p))  # Output: Person('Alice', 30)

# Directly typing the object in the console -> Calls __repr__()
p  # Output: Person('Alice', 30)

🔥 Best Practice:
- Implement both __str__ and __repr__ in your classes.
- Make __repr__ precise and useful for debugging.
- Make __str__ more readable for end users.

🌟 Quick Recap:
- __str__() -> For end-user (Readable)
- __repr__() -> For developers (Detailed & Debugging)
"""

'''

"""
📌 DETAILED DIFFERENCE BETWEEN __str__ AND __repr__ IN PYTHON

🔑 What is __repr__?
1. Purpose:
   - To provide a *developer-friendly* representation of an object.
   - The goal is to be as *precise and unambiguous* as possible.
2. When is it used?
   - When calling repr() on the object.
   - When printing the object directly in the console.
   - As a fallback when __str__() is not defined.
3. Output:
   - Should return a *valid Python expression* that ideally could be used to recreate the object.
   - Commonly used for *debugging and logging*.

📝 Syntax:
def __repr__(self):
    return "ClassName(param1, param2)"

🔑 What is __str__?
1. Purpose:
   - To provide a *user-friendly* representation of an object.
   - The goal is to be *readable and presentable* for end users.
2. When is it used?
   - When calling str() on the object.
   - When using the print() function.
3. Output:
   - Should be *informative and easy to read*.
   - Focuses more on giving a human-readable output.

📝 Syntax:
def __str__(self):
    return "Description of the object"

=========================================================
🔍 EXAMPLE - Understanding the Difference

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person('{self.name}', {self.age})"

    def __str__(self):
        return f"{self.name} (Age: {self.age})"

# Creating an instance of Person
p = Person("Alice", 30)

# Using print() -> Calls __str__()
print("Using print():", p)  # Output: Alice (Age: 30)

# Using str() -> Calls __str__()
print("Using str():", str(p))  # Output: Alice (Age: 30)

# Using repr() -> Calls __repr__()
print("Using repr():", repr(p))  # Output: Person('Alice', 30)

# Directly calling the object in console -> Calls __repr__()
p  # Output: Person('Alice', 30)

=========================================================
🔧 WHY DO WE NEED BOTH?
- The main reason for having both methods is to serve *different purposes*:
  1. __repr__() is for *developers* to get an *unambiguous and accurate representation* of the object.
  2. __str__() is for *end users* to get a *more readable and friendly output*.
- If a class has only __repr__(), and not __str__(), __repr__() will be used as a fallback in both cases.

=========================================================
🚀 BEST PRACTICE
- Always implement __repr__() to provide a *complete and accurate description* for debugging.
- Implement __str__() to give a *clear and readable* representation when printing.
- If you can implement only one, prefer __repr__() because it can serve both purposes.
- Make sure __repr__() returns a *valid Python expression* that can recreate the object if possible.

=========================================================
🌟 QUICK SUMMARY:
1. __repr__() is meant for *developers* (detailed and unambiguous).
2. __str__() is meant for *users* (readable and friendly).
3. If only __repr__() is implemented, it will be used as a fallback for __str__().
4. __repr__() should ideally return a *valid Python expression*.
"""

#OPERATOR OVERLOADING
'''
"""
📌 OPERATOR OVERLOADING IN PYTHON

🔑 What is Operator Overloading?
- Operator overloading allows using the same operator for different data types.
- Python does not limit operators to only work with built-in types.
- You can define how operators like +, -, *, / work with user-defined objects.
- The behavior of an operator is defined using *magic methods* (dunder methods).

=========================================================
✨ WHY OPERATOR OVERLOADING?
1. To make user-defined objects work with operators.
2. To simplify code and improve readability.
3. To enable mathematical operations on objects.
4. To give custom meaning to operators for objects.

=========================================================
📝 HOW DOES IT WORK?
- The operator you want to overload has a corresponding *magic method*.
- You define these magic methods in your class.
- Python automatically calls the appropriate method when the operator is used.

=========================================================
🔧 COMMON OPERATOR OVERLOADING METHODS:
1. Arithmetic Operators:
   - __add__(self, other)       -> Addition (+)
   - __sub__(self, other)       -> Subtraction (-)
   - __mul__(self, other)       -> Multiplication (*)
   - __truediv__(self, other)   -> Division (/)
   - __floordiv__(self, other)  -> Floor Division (//)
   - __mod__(self, other)       -> Modulus (%)
   - __pow__(self, other)       -> Exponent (**)

2. Comparison Operators:
   - __eq__(self, other)        -> Equal (==)
   - __ne__(self, other)        -> Not Equal (!=)
   - __lt__(self, other)        -> Less Than (<)
   - __le__(self, other)        -> Less Than or Equal (<=)
   - __gt__(self, other)        -> Greater Than (>)
   - __ge__(self, other)        -> Greater Than or Equal (>=)

3. Assignment Operators:
   - __iadd__(self, other)      -> In-Place Addition (+=)
   - __isub__(self, other)      -> In-Place Subtraction (-=)
   - __imul__(self, other)      -> In-Place Multiplication (*=)
   - __idiv__(self, other)      -> In-Place Division (/=)

4. Unary Operators:
   - __neg__(self)              -> Negation (-)
   - __pos__(self)              -> Unary Plus (+)
   - __abs__(self)              -> Absolute Value (abs())

=========================================================
🔍 EXAMPLE 1: Overloading Arithmetic Operators
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

p1 = Point(2, 3)
p2 = Point(4, 5)

print("Addition of Points:", p1 + p2)  # Output: (6, 8)
print("Subtraction of Points:", p1 - p2)  # Output: (-2, -2)

================================================

'''

'''
"""
📌 UNDERSTANDING THE 'OTHER' PARAMETER IN OPERATOR OVERLOADING

🔑 WHAT IS 'OTHER' IN OPERATOR OVERLOADING?
- The 'other' parameter in dunder methods (like __add__, __sub__, etc.) represents:
  1. The second operand involved in the operation.
  2. The object on the right side of the operator.

📝 HOW IT WORKS:
- When performing an operation like obj1 + obj2:
  1. obj1 is passed as 'self'.
  2. obj2 is passed as 'other'.
- Python internally calls: obj1.__add__(obj2)

💡 EXAMPLE:
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        # Here 'other' is the second operand (another Point object)
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

p1 = Point(3, 4)
p2 = Point(1, 2)
p3 = p1 + p2  # Internally calls p1.__add__(p2)
print("Sum of Points:", p3)  # Output: (4, 6)

=========================================================
🔧 HOW DOES PYTHON KNOW THAT 'OTHER' IS AN OBJECT?
- Python doesn't know in advance whether 'other' is an object or not.
- It just passes whatever is on the right-hand side of the operator.
- It is up to the programmer to handle the 'other' properly.

📝 HANDLING DIFFERENT TYPES:
- You can use isinstance() to check the type of 'other' before performing operations.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        else:
            raise TypeError("Operand must be a Point object")

p1 = Point(3, 4)
p2 = Point(5, 6)

# Correct usage
print(p1 + p2)  # Output: (8, 10)

# Incorrect usage
try:
    print(p1 + 5)  # Raises: TypeError: Operand must be a Point object
except TypeError as e:
    print("Error:", e)

=========================================================
🌟 WHY IS IT NAMED 'OTHER'?
- The name 'other' is just a convention to indicate the *second operand*.
- You can name it anything (like obj, operand, or anything else).
- However, using 'other' makes the purpose clear and is widely accepted.

=========================================================
🔥 KEY TAKEAWAYS:
1. 'self' represents the current object (left operand).
2. 'other' represents the second operand (right operand).
3. Python doesn't enforce 'other' to be an object, so you need to handle it carefully.
4. Use 'isinstance()' to check the type and avoid unexpected errors.
5. Naming it 'other' is a convention, not a rule.

🎯 QUICK RECAP:
- 'other' is used in operator overloading to represent the second operand.
- Always handle the 'other' parameter carefully to ensure valid operations.
- Use type checking to make your code robust and error-free.
"""

'''

'''
🎯 Tasks (Push to GitHub):
☑ Implement __str__ & __repr__ in Book class.
☑ Implement + operator overloading in Vector class.
'''

class Book:
    def __init__(self, name):
        self.name = name 

    def __str__(self):
        return f"Name of the book: {self.name}"
    
    def __repr__(self):
        return f"Name : {self.name}"
    
b1 = Book('Dunder')
print(b1)  #By default str method is returned or also we can call like this print(str(b1))
print(repr(b1))

class Vector:
    def __init__(self,a,b):
        self.a = a
        self.b = b 

    def __add__(self,other):
        return Vector(self.a+other.a, self.b+other.b)
    
    def __str__(self):
        return f"Vector({self.a},{self.b})"
    
v1 = Vector(2,4)
v2 = Vector(4,8)
v = v1+v2
print(v) #with str method if we print we get memory location as output like this
#<__main__.Vector object at 0x0000016D5BE75910>

#so define str method