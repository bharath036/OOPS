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

#Differences between metaclasses and decorators