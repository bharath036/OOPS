'''
📌 Concepts:
✅ Metaclasses (type(), __new__)
✅ Reflection & Introspection (dir(), hasattr())

🎯 Tasks (Push to GitHub):
☑ Create a Metaclass that auto-capitalizes all class attributes.
☑ Implement a dynamic class that lists all its methods & attributes.

🎯 Mini Project:
☑ Dynamic ORM Model Generator - Use metaclasses to auto-generate Django-like ORM models.

🔗 Resources:

Metaclasses Explained

GitHub Repo: [Your Repo Link]
'''
#Metaclasses
'''
class define how objects behave.., metaclasses define how classes behave

what is type?
Type is the default metaclass in python

The built-in type class has following arguments:
type(name,base,attributes)

-->name is a string containing the name of the class
-->base is a tuple containing base classes for the new class.
-->Attributes is a dictionary pairing the attributes names with their corresponding values.
'''
'''
class Edureka:
    pass 

a = Edureka()
print(type(Edureka)) #output: <class 'type'>
print(type) #output: <class 'type'>
print(type())  #It throws error and says it takes one or 3 arguments
'''
'''
a = type('python',(),{})
print(type(a)) #output: <class 'type'> .., here we have doubt it returns class type as we haven't created class.., check it

print(type) #<class 'type'>
print(type(a())) #<class '__main__.python'>
'''

#Creating custom metaclass in python
'''
A custom metaclass gives us the liberty to decide how the class will behave
'''
#Custom metaclass can also be defined in one of 2 ways

'''
class MetaOne(type):
    def __new__(cls,name,bases,dict):
        pass 
    
class MetaTwo(type):
    def __init__(cls,name,bases,dict):
        pass 

#The __new__ method creates and returns the new class object.
#Then the __init__ method initializes the newly created object.

class Meta(type):
    pass 
class edureka(metaclass=Meta):
    pass 

print(type(edureka)) #<class '__main__.Meta'>

#Differences between metaclasses and decorators'
'''
###############################################################################################
#__new() and __init__() special methods
'''
"""
📌 __new__() vs __init__() in Python

🔧 What is __new__()?
- `__new__()` is a special method responsible for *creating and returning* a new instance of a class.
- It is the *first step* in the object creation process.
- It is called *before* `__init__()`.
- It returns the newly created object instance.

📝 Syntax:
def __new__(cls, *args, **kwargs):
    # Allocate memory and return the object instance
    return super().__new__(cls)

🔑 Key Points:
1. Always takes `cls` (class) as its first parameter.
2. Used mainly in:
   - Singleton patterns (ensuring only one instance exists).
   - Immutable objects (like tuples and strings).
   - Controlling object creation in metaclasses.
3. Must return an instance of the class. If it returns `None`, the object is not created.

🔧 What is __init__()?
- `__init__()` is a special method used to *initialize* the object's attributes.
- It is called *after* the object is created.
- It does *not return anything* (implicitly returns `None`).

📝 Syntax:
def __init__(self, *args, **kwargs):
    # Initialize attributes
    self.attribute = value

=========================================================
🔍 Example to Understand the Flow:
class MyClass:
    def __new__(cls, *args, **kwargs):
        print("Creating instance using __new__()")
        instance = super().__new__(cls)
        return instance
    
    def __init__(self, value):
        print("Initializing instance using __init__()")
        self.value = value

obj = MyClass(10)

# Output:
# Creating instance using __new__()
# Initializing instance using __init__()

=========================================================
🌟 How __new__() and __init__() Work Together:
1. `__new__()` is called to create a new instance.
2. The instance returned by `__new__()` is passed as `self` to `__init__()`.
3. `__init__()` initializes the created instance.

🔑 Practical Use Case - Singleton Pattern:
class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            print("Creating Singleton instance")
            cls._instance = super().__new__(cls)
        return cls._instance

s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # Output: True

=========================================================
🚩 Differences Between __new__() and __init__():
1. __new__() is used to *create* an object, while __init__() is used to *initialize* it.
2. __new__() returns a new instance, whereas __init__() does not return anything.
3. __new__() is called *before* __init__() during object creation.
4. __new__() is useful for *customizing object creation*, especially in immutable types or metaclasses.
5. __init__() is useful for *setting attributes* and *initializing the state*.

🎯 Quick Recap:
- __new__(): Creates and returns a new object.
- __init__(): Initializes the newly created object.
- Both methods work together to make object creation and initialization seamless.
- Use __new__() when you need to control how the object is created.
- Use __init__() when you only need to set attributes or perform post-creation setup.
"""

'''
################################################################################################

'''
📌 Metaclasses in Python - Complete Notes

🔑 What are Metaclasses?
- Metaclasses are classes of classes. They define how classes behave.
- A class itself is an instance of a metaclass.
- Just as objects are created using classes, classes are created using metaclasses.

✨ Why Use Metaclasses?
1. To control how classes are created.
2. To modify or customize class creation.
3. To enforce rules or create APIs.
4. To add methods or attributes to classes during creation.

=========================================================
📝 Basics of Metaclasses:
- In Python, everything is an object, including classes.
- The type() function can be used to check the metaclass of a class.
- The default metaclass is 'type'.

🔧 Example:
class MyClass:
    pass

print(type(MyClass))  # Output: <class 'type'>

=========================================================
🌟 Creating Custom Metaclasses:
- A metaclass is usually created by inheriting from 'type'.
- You can override methods like __new__() and __init__() to customize behavior.

📝 Example:
class Meta(type):
    def __new__(cls, name, bases, dct):
        print(f'Creating class: {name}')
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=Meta):
    pass

# Output: Creating class: MyClass

=========================================================
⚙️ Metaclass Workflow:
1. Python sees 'metaclass=Meta' while creating MyClass.
2. Calls Meta.__new__() to create the class object.
3. Returns the created class.

=========================================================
💡 Using Metaclasses for Class Customization:
- Metaclasses can be used to enforce class rules or add common behavior.

🔍 Example:
class Meta(type):
    def __new__(cls, name, bases, dct):
        if 'greet' not in dct:
            raise TypeError('Class must have a greet method')
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=Meta):
    def greet(self):
        return 'Hello!'

obj = MyClass()
print(obj.greet())  # Output: Hello!

=========================================================
🚀 Practical Uses of Metaclasses:
1. Singleton Pattern:
   - Ensures only one instance of a class is created.

2. Class Registration:
   - Automatically register classes for future use.

3. Class Validation:
   - Enforce the presence of mandatory methods or attributes.

=========================================================
🌟 Key Points to Remember:
1. Metaclasses define how classes behave.
2. The default metaclass in Python is 'type'.
3. Use metaclasses to customize class creation.
4. Metaclasses can add, modify, or enforce methods and attributes.
5. Metaclasses are an advanced feature - use them wisely and when needed.

🎯 Quick Recap:
- Metaclasses are classes for classes.
- They control how classes are constructed and behave.
- Use cases include enforcing rules, adding behavior, and creating singletons.

'''
######################################################################################################
'''
📌 Metaclasses in Python - Complete Notes

🔑 What are Metaclasses?
- Metaclasses are classes of classes. They define how classes behave.
- A class itself is an instance of a metaclass.
- Just as objects are created using classes, classes are created using metaclasses.

✨ Why Use Metaclasses?
1. To control how classes are created.
2. To modify or customize class creation.
3. To enforce rules or create APIs.
4. To add methods or attributes to classes during creation.

=========================================================
📝 Basics of Metaclasses:
- In Python, everything is an object, including classes.
- The type() function can be used to check the metaclass of a class.
- The default metaclass is 'type'.

🔧 Example:
class MyClass:
    pass

print(type(MyClass))  # Output: <class 'type'>

=========================================================
🌟 Creating Custom Metaclasses:
- A metaclass is usually created by inheriting from 'type'.
- You can override methods like __new__() and __init__() to customize behavior.

📝 Example:
class Meta(type):
    def __new__(cls, name, bases, dct):
        print(f'Creating class: {name}')
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=Meta):
    pass

# Output: Creating class: MyClass

=========================================================
⚙️ Metaclass Workflow:
1. Python sees 'metaclass=Meta' while creating MyClass.
2. Calls Meta.__new__() to create the class object.
3. Returns the created class.

=========================================================
💡 Real World Example: Singleton Pattern
- Singleton pattern ensures that a class has only one instance.
- A metaclass can be used to enforce the singleton behavior.

🔍 Real World Example (Singleton):
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class DatabaseConnection(metaclass=SingletonMeta):
    def connect(self):
        print("Database connected")

# Usage
conn1 = DatabaseConnection()
conn2 = DatabaseConnection()
print(conn1 is conn2)  # Output: True (Same instance)

🚀 Where to Use Metaclasses:
1. Creating Singletons: Ensure only one instance of a class.
2. Enforcing Class Attributes: Make sure certain attributes or methods are present in every class.
3. Class Registration: Automatically keep track of all subclasses.
4. Code Injection: Add or modify methods during class creation.
5. API Development: Enforce specific structure and behavior.

=========================================================
🌟 Key Points to Remember:
1. Metaclasses define how classes behave.
2. The default metaclass in Python is 'type'.
3. Use metaclasses to customize class creation.
4. Metaclasses can add, modify, or enforce methods and attributes.
5. Metaclasses are an advanced feature - use them wisely and when needed.

🎯 Quick Recap:
- Metaclasses are classes for classes.
- They control how classes are constructed and behave.
- Use cases include enforcing rules, adding behavior, and creating singletons.

'''
#############################################################
#Meta classes in Django models
'''
=========================================================
🌐 Metaclasses in Django Models:

🔑 Why are Metaclasses Used in Django Models?
- Django uses metaclasses to create model classes with specific behavior.
- It uses the metaclass to automatically create fields and add metadata to the model.
- It also registers models within the application without manually declaring them.

📝 How It Works in Django:
- Django models use `ModelBase` as a metaclass, which is a subclass of `type`.
- This metaclass handles the creation of fields, metadata, and database table names.

🔍 Example:
from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

# Usage
person = Person(name="John", age=25)
print(person)

💡 Behind the Scenes:
1. When the `Person` class is defined, the `ModelBase` metaclass takes over.
2. It collects the field definitions (name, age) and stores them in the `_meta` attribute.
3. Automatically generates methods like `save()`, `delete()`, and the database table name.
4. Registers the model with Django's internal system for use with the ORM.

🚀 Real-World Impact:
- Simplifies model creation and database interactions.
- Automatically handles complex ORM tasks, allowing developers to focus on business logic.
- Enables powerful introspection and dynamic behavior without writing boilerplate code.

🌟 Why Metaclasses Are Crucial for Django:
1. Automation of Model Registration: Models are registered without manual intervention.
2. Database Table Mapping: Dynamically creates table names and mappings.
3. Field and Metadata Handling: Manages field definitions and associated metadata.
4. ORM Operations: Provides methods for CRUD operations automatically.

📝 Quick Recap:
- Django leverages metaclasses to make ORM easy and dynamic.
- Metaclasses in Django handle automatic model registration and field mapping.
- This powerful feature reduces manual work and enforces consistency.


'''
#############################################################################################
#Meta classes type() and new()
'''
=========================================================
🛠️ Metaclasses: type() and __new__()

🔑 What is type() in Metaclasses?
- The built-in `type()` function in Python serves two purposes:
  1. **Type Checking:** Returns the type of an object.
     Example: `print(type(10))`  # Output: <class 'int'>
  2. **Dynamic Class Creation:** Acts as a metaclass when called with three arguments.

📝 Dynamic Class Creation with type():
- Syntax: `type(class_name, bases, attributes)`
  - `class_name`: Name of the new class.
  - `bases`: A tuple containing the base classes.
  - `attributes`: A dictionary of attributes and methods.

🔍 Example:
MyClass = type('MyClass', (object,), {'x': 5, 'greet': lambda self: print("Hello")})
obj = MyClass()
print(obj.x)  # Output: 5
obj.greet()   # Output: Hello

=========================================================
🔧 __new__() Method in Metaclasses:
- The `__new__()` method is responsible for creating and returning a new instance of a class.
- It is the first step in object creation, even before `__init__()`.
- In metaclasses, `__new__()` is used to control how classes themselves are created.

📝 Syntax:
class Meta(type):
    def __new__(cls, name, bases, dct):
        print(f'Creating class: {name}')
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=Meta):
    pass

# Output: Creating class: MyClass

=========================================================
🌟 Why Use __new__() in Metaclasses?
1. To customize the creation of classes.
2. To add or modify methods and attributes dynamically.
3. To enforce constraints or validation while creating classes.
4. To automatically register classes during creation.

🚀 Key Differences Between __new__() and __init__():
- `__new__()` is responsible for creating and returning the object instance.
- `__init__()` initializes the object after it is created.
- `__new__()` is called first, followed by `__init__()`.

🔍 Example:
class SingletonMeta(type):
    _instances = {}

    def __new__(cls, name, bases, dct):
        if name in cls._instances:
            return cls._instances[name]
        instance = super().__new__(cls, name, bases, dct)
        cls._instances[name] = instance
        return instance

class SingletonClass(metaclass=SingletonMeta):
    pass

obj1 = SingletonClass()
obj2 = SingletonClass()
print(obj1 is obj2)  # Output: True

=========================================================
💡 Quick Recap:
1. `type()` is used for both type checking and dynamic class creation.
2. `__new__()` is responsible for creating the class instance itself.
3. Metaclasses leverage `__new__()` to control class creation and enforce rules.
4. Combining `type()` and `__new__()` allows for advanced customization of class behavior.


'''

#Reflection and Introspection in python
'''
"""
📌 Reflection & Introspection in Python

🔍 What is Reflection?
- Reflection is the ability of a program to inspect and manipulate its own structure and behavior at runtime.
- In Python, it means inspecting classes, methods, and objects while the program is running.

🔧 What is Introspection?
- Introspection is the process of examining the type and attributes of an object at runtime.
- It allows us to gather information about the object without knowing its details beforehand.

=========================================================
🛠️ Reflection in Python - Key Functions:

1. dir() - Lists all the attributes and methods of an object.
2. hasattr() - Checks if an object has a specific attribute.
3. getattr() - Gets the value of a specified attribute.
4. setattr() - Sets the value of a specified attribute.
5. type() - Returns the type of an object.
6. isinstance() - Checks if an object is an instance of a class or a subclass.

=========================================================
🔧 Introspection Using dir():
- The dir() function returns a list of valid attributes and methods of an object.

🔍 Example:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, I am {self.name}")

p = Person("Alice", 30)
print(dir(p))

# Output (Partial):
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', 
#  '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__',
#  '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', 
#  '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', 
#  '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 
#  'age', 'greet', 'name']

=========================================================
🔧 Checking Attributes Using hasattr():
- The hasattr() function checks whether an object has a given attribute.

🔍 Example:
print(hasattr(p, 'name'))  # Output: True
print(hasattr(p, 'address'))  # Output: False

🔧 Getting Attribute Value Using getattr():
- The getattr() function retrieves the value of a specified attribute.
print(getattr(p, 'name'))  # Output: Alice
print(getattr(p, 'address', 'Not Found'))  # Output: Not Found

🔧 Setting Attribute Value Using setattr():
- The setattr() function sets or updates the value of an attribute.
setattr(p, 'age', 35)
print(p.age)  # Output: 35

=========================================================
🔧 Getting the Type of an Object Using type():
- The type() function returns the type of the object.
print(type(p))  # Output: <class '__main__.Person'>

🔧 Checking Instance Type Using isinstance():
- The isinstance() function checks whether an object is an instance of a specific class.
print(isinstance(p, Person))  # Output: True

=========================================================
🌟 Practical Use Cases:
1. **Dynamic Attribute Access:** Dynamically setting or getting object attributes.
2. **Debugging and Testing:** Examining object properties during testing.
3. **Serialization and Deserialization:** Dynamically identifying fields to serialize.
4. **Dynamic Method Invocation:** Calling methods that are determined at runtime.

=========================================================
🔥 Key Takeaways:
1. Reflection enables dynamic inspection and manipulation of objects.
2. Introspection helps examine object attributes, methods, and types at runtime.
3. Use dir() to list attributes and methods.
4. Use hasattr() to check if an attribute exists.
5. Use getattr() and setattr() for dynamic attribute access.
6. Use type() and isinstance() for type inspection.

🎯 Quick Recap:
- Reflection and Introspection are powerful features that make Python dynamic and flexible.
- They are useful for debugging, testing, and dynamically manipulating objects.
"""

'''
#####################################################################################################
#In simple words
'''
"""
📌 Reflection & Introspection in Python (Simple Words)

🔑 What is Reflection?
- Reflection means looking at your own code while it is running.
- It helps the program examine and modify itself at runtime.

🔑 What is Introspection?
- Introspection means finding out what an object can do or what it contains.
- It helps you learn about the object's type, methods, and attributes.

=========================================================
🔧 Useful Functions for Reflection & Introspection:

1. dir() - Shows all methods and attributes of an object.
2. hasattr() - Checks if an object has a specific attribute.
3. getattr() - Gets the value of an attribute.
4. setattr() - Sets or updates the value of an attribute.
5. type() - Tells you the type of an object.
6. isinstance() - Checks if an object belongs to a specific class.

=========================================================
🔍 Using dir() to See What an Object Can Do:
class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year
    
    def drive(self):
        print("Driving")

car = Car("Mustang", 2020)

print(dir(car))  # Lists all methods and attributes of car object

=========================================================
🔍 Checking Attributes with hasattr():
print(hasattr(car, 'model'))  # True (car has a 'model' attribute)
print(hasattr(car, 'color'))  # False (car has no 'color' attribute)

🔍 Getting the Value of an Attribute with getattr():
print(getattr(car, 'model'))  # Output: Mustang
print(getattr(car, 'color', 'Not Found'))  # Output: Not Found

🔍 Setting or Updating an Attribute with setattr():
setattr(car, 'color', 'Red')  # Adds or updates the 'color' attribute
print(car.color)  # Output: Red

=========================================================
🔍 Getting the Type of an Object with type():
print(type(car))  # Output: <class '__main__.Car'>

🔍 Checking if an Object Belongs to a Class with isinstance():
print(isinstance(car, Car))  # Output: True

=========================================================
🌟 Real-Life Uses:
1. Debugging: Check what methods and attributes an object has.
2. Dynamic Access: Get or set attributes at runtime.
3. Serialization: Easily find out what to save from an object.
4. Flexible Code: Handle different types of objects without knowing them in advance.

🔥 Quick Recap:
- Reflection: Looking at your code while it runs.
- Introspection: Finding out what an object has and can do.
- Use dir() to see available methods and attributes.
- Use hasattr() to check if an attribute exists.
- Use getattr() and setattr() to get or set attributes.
- Use type() and isinstance() to check the type of an object.

📝 Summary:
Reflection and introspection make your code flexible and dynamic. You can inspect and change objects on the fly, making Python super powerful and adaptable!
"""

'''

##################################################################################################################################################################
#Difference

'''
"""
📌 Difference between Reflection and Introspection

🔑 Reflection:
- Reflection is the ability of a program to examine and modify its own structure and behavior at runtime.
- It allows the program to manipulate objects and classes dynamically.
- Reflection involves:
  1. Creating objects dynamically.
  2. Modifying or adding new methods.
  3. Changing attributes during execution.
- Mainly used to:
  1. Dynamically create and modify objects.
  2. Change class definitions or add methods on the fly.

🔧 Example:
class MyClass:
    pass

obj = MyClass()
setattr(obj, 'name', 'Python')  # Adding an attribute dynamically
print(obj.name)  # Output: Python

=========================================================
🔑 Introspection:
- Introspection is the ability of a program to examine the type and properties of objects at runtime.
- It helps in finding out what methods or attributes an object has.
- Introspection involves:
  1. Inspecting methods and attributes.
  2. Checking types and instances.
  3. Getting metadata of an object.
- Mainly used to:
  1. Check object properties before using them.
  2. Dynamically explore objects.
  3. Make the code adaptive and flexible.

🔧 Example:
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Alice")
print(hasattr(p, 'name'))  # Output: True
print(dir(p))  # Lists all methods and attributes

=========================================================
🌟 Key Differences:

1. **Purpose:**
   - Reflection: Modify and manipulate objects or classes.
   - Introspection: Inspect and gather information about objects.

2. **Usage:**
   - Reflection: Creating, modifying, and adding new methods or attributes at runtime.
   - Introspection: Checking attributes, methods, and object types.

3. **Focus:**
   - Reflection: Changing object behavior.
   - Introspection: Checking object properties.

4. **Examples:**
   - Reflection: `setattr()`, `type()`, `__new__()`.
   - Introspection: `hasattr()`, `dir()`, `isinstance()`, `getattr()`.

=========================================================
🔥 Summary:
- Reflection is about *changing* or *modifying* objects or classes dynamically.
- Introspection is about *inspecting* and *understanding* what objects are made of.
- Both concepts make Python dynamic and flexible, allowing for powerful object manipulation and inspection.

🎯 Quick Recap:
- Reflection: Change and manipulate.
- Introspection: Inspect and analyze.
- Use both wisely to make your code dynamic and adaptive!
"""

'''

#Tasks
'''
☑ Create a Metaclass that auto-capitalizes all class attributes.
☑ Implement a dynamic class that lists all its methods & attributes.

'''

# 🎯 Task 1: Metaclass to Auto-Capitalize All Class Attributes
class CapitalizeAttributes(type):
    def __new__(cls, name, bases, dct):
        capitalized_attrs = {}
        for key, value in dct.items():
            if not key.startswith('__'):
                capitalized_attrs[key.upper()] = value
            else:
                capitalized_attrs[key] = value
        return super().__new__(cls, name, bases, capitalized_attrs)

class Employee(metaclass=CapitalizeAttributes):
    name = "John"
    position = "Manager"

# Checking the capitalized attributes
print("Capitalized Attributes:")
print(hasattr(Employee, 'NAME'))     # Output: True
print(hasattr(Employee, 'POSITION')) # Output: True

print("Accessing Attributes:")
print(Employee.NAME)     # Output: John
print(Employee.POSITION) # Output: Manager

print("\n=========================================\n")

# 🎯 Task 2: Dynamic Class that Lists All Its Methods & Attributes
class DynamicInfo:
    def list_methods(self):
        return [method for method in dir(self) if callable(getattr(self, method)) and not method.startswith("__")]

    def list_attributes(self):
        return [attr for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith("__")]

class Person(DynamicInfo):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hello, I am {self.name}")

p = Person("Alice", 30)

print("Dynamic Class Methods:")
print(p.list_methods())  # Output: ['greet', 'list_attributes', 'list_methods']

print("\nDynamic Class Attributes:")
print(p.list_attributes())  # Output: ['age', 'name']

