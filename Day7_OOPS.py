#Design Patterns (Singleton,Factory,Observer)
'''
📌 Concepts:
✅ Singleton Pattern
✅ Factory Pattern
✅ Observer Pattern

🎯 Tasks (Push to GitHub):
☑ Implement a Logger Class (Singleton Pattern).
☑ Implement a Shape Factory (Factory Pattern).

🎯 Mini Project:
☑ Real-time Notification System (Observer Pattern) - Notify users when a new product is added.

🔗 Resources:

Python Design Patterns

GitHub Repo: [Your Repo Link]
'''

'''
🚀 Design Patterns - Simplified Explanation
📌 What are Design Patterns?
Design patterns are like templates for solving common programming problems.

They are best practices that help you write clean and efficient code.

They make your code more reusable, flexible, and maintainable.

✅ 1. Singleton Pattern
🔑 What is it?
The Singleton pattern ensures that a class has only one instance and provides a global access point to it.

Imagine a Database Connection object that you want to reuse instead of creating multiple connections.

📝 How it Works:
The Singleton class:

Creates an instance only if one does not already exist.

Returns the existing instance for every subsequent call.

💡 Real-Life Analogy:
Think of a President of a country. There can only be one president at a time.

🔧 Example:
python
Copy
Edit
class Singleton:
    _instance = None  # Class-level attribute

    def __new__(cls):
        if cls._instance is None:
            print("Creating a new instance")
            cls._instance = super().__new__(cls)
        return cls._instance

obj1 = Singleton()
obj2 = Singleton()

print(obj1 is obj2)  # Output: True (both refer to the same instance)
✅ 2. Factory Pattern
🔑 What is it?
The Factory pattern provides a way to create objects without specifying the exact class.

It defines a common interface and allows subclasses to decide which object to create.

💡 Real-Life Analogy:
Think of a Vehicle Factory that can produce Cars, Bikes, or Trucks without you needing to know the internal details.

🔧 Example:
python
Copy
Edit
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            return None

animal1 = AnimalFactory.create_animal("dog")
print(animal1.speak())  # Output: Woof!

animal2 = AnimalFactory.create_animal("cat")
print(animal2.speak())  # Output: Meow!
✅ 3. Observer Pattern
🔑 What is it?
The Observer pattern establishes a one-to-many relationship between objects.

When one object changes state, all its dependents are notified and updated automatically.

Useful for real-time updates like notifications or event handling.

💡 Real-Life Analogy:
Think of a YouTube channel subscription:

You subscribe to a channel (observer).

Whenever a new video is uploaded (event), you get notified.

🔧 Example:
python
Copy
Edit
class Observer:
    def update(self, message):
        pass

class Subscriber(Observer):
    def update(self, message):
        print(f"Notification received: {message}")

class Channel:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def notify(self, message):
        for subscriber in self.subscribers:
            subscriber.update(message)

# Creating channel and subscribers
channel = Channel()
sub1 = Subscriber()
sub2 = Subscriber()

# Subscribing users
channel.subscribe(sub1)
channel.subscribe(sub2)

# Notifying subscribers
channel.notify("New Video Uploaded!")
💡 What Should You Know Before Learning These Patterns:
Object-Oriented Programming (OOP) concepts:

Classes and Objects

Inheritance and Polymorphism

Encapsulation and Abstraction

Dunder Methods (__new__(), __init__()) for Singleton

Factory Methods and Interfaces for Factory Pattern

Event Handling for Observer Pattern

🔥 Quick Recap:
Singleton Pattern: Ensures one instance only. Useful for logging, database connections.

Factory Pattern: Creates objects without specifying exact classes. Useful for object creation without exposing the logic.

Observer Pattern: Allows automatic updates when changes happen. Useful for real-time notifications.
'''

'''
📌 Concepts: Design Patterns in Python

🚀 Introduction:
- Design patterns are typical solutions to common problems in software design.
- They represent best practices and reusable solutions to recurring problems.
- In Python, design patterns help structure and organize code efficiently.
- Three essential design patterns:
  1. Singleton Pattern
  2. Factory Pattern
  3. Observer Pattern

=========================================================
✅ Singleton Pattern:
🔑 Concept:
- Ensures that a class has only one instance and provides a global point of access to it.
- Useful when exactly one object is needed to coordinate actions.

🌟 Use Cases:
1. Database connections
2. Logging systems
3. Configuration managers

🔧 Implementation:
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creating Singleton Instance")
            cls._instance = super().__new__(cls)
        return cls._instance

obj1 = Singleton()
obj2 = Singleton()
print(obj1 is obj2)  # Output: True

📝 Key Takeaways:
- Only one instance is created, even if instantiated multiple times.
- The `__new__()` method ensures single instance creation.

=========================================================
✅ Factory Pattern:
🔑 Concept:
- Provides a way to create objects without specifying the exact class of object that will be created.
- Encapsulates the object creation logic.

🌟 Use Cases:
1. Creating objects of different subclasses
2. Managing and centralizing object creation
3. Reducing direct dependencies on concrete classes

🔧 Implementation:
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError("Unknown animal type")

animal = AnimalFactory.create_animal("dog")
print(animal.speak())  # Output: Woof!

📝 Key Takeaways:
- Decouples object creation from usage.
- Makes adding new types easy without changing existing code.

=========================================================
✅ Observer Pattern:
🔑 Concept:
- Defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.
- Useful for implementing distributed event-handling systems.

🌟 Use Cases:
1. Event handling systems
2. GUI frameworks where multiple elements update on change
3. Real-time data feeds

🔧 Implementation:
class Observer:
    def update(self, message):
        pass

class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

class ConcreteObserver(Observer):
    def update(self, message):
        print("Received update:", message)

subject = Subject()
observer1 = ConcreteObserver()
observer2 = ConcreteObserver()
subject.attach(observer1)
subject.attach(observer2)
subject.notify("Hello Observers!")

📝 Key Takeaways:
- The observer pattern promotes loose coupling between the subject and the observers.
- Ideal for real-time applications and notifications.

=========================================================
🌟 What Should You Know Before Learning These Patterns:
1. Object-Oriented Programming (OOP) Basics
   - Classes, Inheritance, and Polymorphism
   - Encapsulation and Abstraction
2. Understanding of Constructors (`__init__()`)
3. Familiarity with Dunder Methods (`__new__()` for Singleton)
4. Understanding of Design Principles like DRY (Don’t Repeat Yourself)

🎯 Quick Recap:
- Design patterns are solutions to common programming problems.
- Singleton Pattern: Ensures a single instance.
- Factory Pattern: Creates objects without specifying the exact class.
- Observer Pattern: Notifies dependent objects about state changes.
- Mastering these patterns helps you write more organized, reusable, and scalable code.

'''
'''
To get a better understanding of these patterns and their real-world applications, I recommend the following resources:

🚀 1. Official Python Documentation:
Learn about OOP concepts and dunder methods directly from the official source.

Python docs on Data Model

📘 2. Books:
Head First Design Patterns (by Eric Freeman & Elisabeth Robson)

Great for visual learners and beginners.

Uses real-world analogies to explain design patterns.

Design Patterns: Elements of Reusable Object-Oriented Software (by Erich Gamma et al.)

Known as the “Gang of Four (GoF)” book.

A classic, covering 23 design patterns with practical examples.

Though examples are in C++, the concepts are universal.

Python Design Patterns (by Chetan Giridhar)

Focused on implementing design patterns using Python.

Practical examples and explanations.

🎥 3. Video Tutorials (YouTube):
"Singleton Design Pattern" - CodeAcademy and Tech with Tim

Simple and practical examples with Python code.

"Factory Design Pattern" - freeCodeCamp.org

Good for understanding the concept with real-world analogies.

"Observer Design Pattern" - Tech with Tim

Explains how to implement and where to use it.

📝 4. Online Courses (Udemy / Coursera):
"Python Design Patterns" - Udemy

Covers most of the important design patterns with code snippets.

"Design Patterns in Python" by Pluralsight

Focuses on applying design patterns using Python-specific techniques.

🌐 5. Blogs and Articles:
Real Python - Design Patterns Series:

Practical and well-explained Python code for various patterns.

Real Python Design Patterns

GeeksforGeeks - Design Patterns in Python:

Simple explanations with code snippets.

Design Patterns on GfG

📝 6. GitHub Repositories:
Check out repositories that showcase practical use cases and implementations:

Faif/python-patterns - Examples of various design patterns implemented in Python.

Refactoring.Guru - Design pattern explanations and practical examples.

🎯 What You Should Focus On:
Understand the Problem Each Pattern Solves:

Why and when should you use it?

Practice with Real-World Scenarios:

Implement small projects to see how they work in action.

Analyze Existing Codebases:

Look for patterns used in open-source projects on Git
'''