'''
#The repr and str special methods
class Competition:
    def __init__(self,name,prize):
        self.__name = name
        self.__prize = prize

rowing = Competition('Rowing',10000)
print(rowing)
# output:-<__main__.Competition object at 0x00000185F0A6F310>
#Competition represented by name and prize. When an object of class 
#competition is printed this is what we see.
'''
'''
#Using repr
class Competition:
    def __init__(self,name,prize):
        self.__name = name 
        self.__prize = prize

    def __repr__(self):
        return "({},{})".format(self.__name,self.__prize)
    
archery = Competition('Archery',8000)
print(archery)

#output:-(Archery,8000)

If you don't define the __repr__() or __str__() method in a class, Python falls back on the default behavior,
which is to print a generic string that shows the object's type and memory location.
'''
'''
#__repr__(self) --> determines how an object is represented when printed out on screen
repr(archery) #prints string representation but no output executed

print(repr(archery)) #prints string representation
#output:(Archery,8000)

#str(archery) #looks for a string representation in the __str__() then the __repr__() function
print(str(archery))
'''
'''
class Competition:
    def __init__(self,name,prize,country):
        self.__name = name 
        self.__country = country
        self.__prize = prize 

    def get_name_country(self):
        return '{}-{}'.format(self.__name,self.__country)
    
    def __repr__(self):
        return "Competition:{} held in {},prize:{}".format(self.__name,self.__country,self.__prize)
    
    def __str__(self):
        return '{}-{}'.format(self.get_name_country(),self.__prize)
#IT FIRST CALLS STR METHOD TO REPRESENT
archery = Competition('Archery', 7500 , 'UK')
print(archery) #output:Archery7500-UK
print(repr(archery)) #output:Competition:Archery held in 7500,prize:UK
archery 

'''


#The add special method
#int __add__(1,3) we can't directly use it we have to define in a class/as a method and use it
'''
class Savings:
    def __init__(self,amount):
        self.__amount = amount

S1 = Savings(1000)
S2 = Savings(2000)

S1+S2 #We get error as we cannot add 2 objects

'''
'''
class Savings:
    def __init__(self,amount):
        self.__amount = amount

    def __add__(self,other):
        return self.__amount + other.__amount
    
s1 = Savings(1000)
s2 = Savings(2000)
s3 = Savings(4000)

s1+s2  #we have to print it so we have to use print function and first assign to a variable to store the value and print
print(s1+s2) 
s=s1+s2 
print(s)
'''
'''
#The sub special method

class Methodsub:
    def __init__(self,number):
        self.__number = number 

    def __sub__(self,other):
        return self.__number - other.__number 
    
num_1 = Methodsub(10)
num_2 = Methodsub(7)
result = num_1 - num_2
print(result)

#if we redefine above __sub__ method with * , in the result it will multiply 
#and gives result. If we multiply 2 objects it throws error
#see below example

class Methodsub:
    def __init__(self,number):
        self.__number = number 

    def __sub__(self,other):
        return self.__number * other.__number 
    
num_1 = Methodsub(10)
num_2 = Methodsub(7)
result = num_1 * num_2
print(result)

#The error occurs because you are trying to use the multiplication operator (*) with instances of the Methodsub class
#, but you have only defined the __sub__ method, which is for the subtraction operator (-).
'''

#The mul special method 
'''
class Methodsub:
    def __init__(self, number):
        self.__number = number 

    def __mul__(self, other):
        return self.__number * other.__number 

num_1 = Methodsub(10)
num_2 = Methodsub(7)
result = num_1 * num_2
print(result)  # Output: 70

'''
'''
class Savings:
    def __init__(self,amount):
        self.__amount = amount
    
    def __add__(self,other):
        return self.__amount + other.__amount
    
    def __mul__(self,other):
        if type(other) == int or type(other)== float:
            return self.__amount*other 
        else:
            raise ValueError("Can't multiply by int or float")
        
s1 = Savings(1000)
s2 = Savings(22)

add = s1+s2 
print(add)
        
#print(s1*s2) #throws error

print(s1*3)

'''

#Special methods for other operations 
#Floordiv // 
'''
class MethodFloordiv:
    def __init__(self,number):
        self.__number = number 
    
    def __floordiv__(self,other):
        return self.__number//other.__number 
    
number_1 = MethodFloordiv(10)
number_2 = MethodFloordiv(3)

a = number_1//number_2
print(a)
'''

#mod gives remainder when one number is divided by other method
'''
class Methodmod:
    def __init__(self,number):
        self.__number = number 
    
    def __mod__(self,other):
        return self.__number % other.__number
    

num_1 = Methodmod(10)
num_2 = Methodmod(3)

a = num_1%num_2 
print(a)

'''

#Power of 2 numbers
'''
class Methodpow:
    def __init__(self,number):
        self.__number = number

    def __pow__(self,other):
        return self.__number ** other.__number 
    
num_1 = Methodpow(10)
num_2 = Methodpow(2)
a = num_1**num_2
print(a)

'''

#Built-in functions and custom data types
#Not only mathematical operators but it also supports built-in functions
#python lists belong to the list built-in class.The list class has an implementation for the __len__() special method.
'''
len('test')
str.__len__('test')
'''
'''
class Participants:
    def __init__(self):
        self.__participants = []

    def add__participants(self,name):
        self.__participants.append(name)

    def __len__(self):
        return len(self.__participants)
    
p = Participants()
print(len(p))


p.add__participants('James')
p.add__participants('Tom')
print(len(p))

'''
#Custom iterators using special methods
'''
some_list = [1,2,3,4]

for num in some_list:
    print(num)
'''

'''
class Participants:
    def __init__(self):
        self.__participants = []
        self.__index = 0

    def add_participants(self,name):
        self.__participants.append(name)

    def __len__(self):
        return len(self.__participants)
    
    def __iter__(self):  #The __iter__ method resets the index for a new iteration and returns the instance itself.
        self.__index = 0
        return self  #Try to understand
    
    def __next__(self):
        if self.__index == len(self.__participants):
            raise StopIteration
        p = self.__participants[self.__index]
        self.__index += 1
        return p 
    
#The class should implement __next__(). An iterator is any object that responds to the __next__() special method.

participants = Participants()
participants.add_participants('lily')
participants.add_participants('john')
participants.add_participants('james')
participants.add_participants('Host')

#down P and p in iter method are not same
for P in participants:
    print(P)

'''

'''
Mistakes done during the code 
Correct the naming of the __len method to __len__ so it follows the special method naming convention.
Fix the typo in the __next__ method where self.__participants(self.__index) should be self.__participants[self.__index]-->this may thinks 
self.__participants is a function and tries to call.
Fix the typo in the __next__ method where self.index += 1 should be self.__index += 1-->this may cause attribute error.
'''

#Defining properties on classes
#getters, setters

'''
from typing import Any


class Wrestler:
    def __init__(self):
        self.__name = " "

    def set_name(self,name):
        self.__name = name 
    
    def get_name(self):
        return print(self.__name)
    
w1 =Wrestler()
w1.set_name("Steveeee")

w1.get_name() #this works as we use print statement in return statement and it prints it.
#we can't directly access w1.name as name is a private variable
print(w1.__dict__)
print(w1._Wrestler__name) 
#w2=w1.__name #it throws error
#print(w1.__dict__)       
'''
'''
#Lets redefine the above class 

class Wrestler:
    def __init__(self):
        self.__name = ''

    def set_name(self,name):
        print("Setter method called")
        self._name = name 

    def get_name(self):
        print('getter method called')
        return self.__name 

    name = property(get_name,set_name)


w =Wrestler()
w.name = 'Kart'
w.name
'''

#Defining properties using decorators
'''
class Wrestler:

    def __init__(self,name):
        self.__name = name 

    @property
    def name(self):
        print('getter method called')
        return self.__name 

    @name.setter
    def name(self,value):
        print('setter method called')
        self.__name = value 

    @name.deleter
    def name(self):
        print('deleter method called')
        del self.__name 

w =Wrestler('Adam')
w.name
w.name = 'John' #setter method called

del w.name 
w.name #this gives attribute error because name attributed is deleted
'''
'''
class Wrestler:

    def __init__(self,name,age):
        self.__name = name 
        self.__age = age

    @property
    def name(self):
        print('name getter method called')
        return self.__name 

    @name.setter
    def name(self,value):
        print('name setter method called')
        self.__name = value 

    @name.deleter
    def name(self):
        print('name deleter method called')
        del self.__name 

    @property
    def age(self):
        print("age getter method called")
        return self.__age 
    
    @age.setter
    def age(self,value):
        print("age setter method called")

    @age.deleter
    def age(self):
        print("age deleter method called")
        del self.__age

w =Wrestler('john',28)
w.name

'''

#There are two other types of methods that are associated with classes
#class methods and static methods  

#class methods
#Associated with the class itself, but not a specific instance or a object of a class
'''
class Competition:
    __raise_amount = 1.04  #class variable

    def __init__(self,name,prize):
        self.__name = name          #this are instance variables
        self.__prize = prize 

    def raise_prize(self):
        self.__prize = self.__prize*self.__raise_amount

    def print_details(self):
        print("Name: {} , Prize: {}".format(self.__name,self.__prize))

    @classmethod
    def get_raise_amount(cls):  #we pass cls for class methods as first argument
        return cls.__raise_amount
    
    @classmethod
    def set_raise_amount(cls,amount):
        cls.__raise_amount = amount

sprint = Competition('Sprint',1000)
sprint.print_details()

sprint.get_raise_amount()

sprint.set_raise_amount(1.07)

#we can pass string as below and split into arguments
swimming_str = 'Swimming-8000'
name,prize = swimming_str.split('-')
swimming = Competition(name,prize)
swimming.print_details()

'''

#Lets redefine swimming str in form of class and see
'''
class Competition:
    __raise_amount = 1.04  #class variable

    def __init__(self,name,prize):
        self.__name = name          #this are instance variables
        self.__prize = prize 

    def raise_prize(self):
        self.__prize = self.__prize*self.__raise_amount

    def print_details(self):
        print("Name: {} , Prize: {}".format(self.__name,self.__prize))

    @classmethod
    def get_raise_amount(cls):  #we pass cls for class methods as first argument
        return cls.__raise_amount
    
    @classmethod
    def set_raise_amount(cls,amount):
        cls.__raise_amount = amount

    @classmethod
    def from_str(cls,competition_str):
        name, prize = competition_str.split('-')

        return cls(name,prize)
    
archery_str = 'Archery-8000'
archery = Competition.from_str(archery_str)
archery.print_details()
'''

#Static methods
'''
static methods doesn't have any reference to class. It is nothing
Static methods are utility methods which have no access to class or instance state
Static methods cannot access any class variables and also instaces
'''

'''
class Rectangle:

    def area(x,y):
        return x*y

Rectangle.area = staticmethod(Rectangle.area) #converting area method to static method in manual way
print('area of rectangle is :', Rectangle.area(15,16))

#in this way also we can make it static method

class Rectangle:

    @staticmethod
    def area(x,y):
        return x*y 
    
print('area of rectangle is :', Rectangle.area(15,16))
'''

#Abstract Base Classes
from abc import ABC, abstractmethod
'''
#base class
class Hominidae:
    def diet(self):  # Here diet, walf functions don't have implementations
        pass 

    def walk(self):
        pass 

    def behavior(self):
        print('They show complex facial expression and social behaviour.')

chimpanzee = Hominidae()
chimpanzee.behavior()

chimpanzee.diet() #no output

#derieved class
#here implementations are given
class Human(Hominidae):

    def diet(self):
        print("Humans are omnivorous.")
    
    def walk(self):
        print("They are bipeds.")
 
paul = Human()
paul.diet()
'''
'''
#ABC is an incomplete class which does not have implementations for all the methods
class Hominidae(ABC):
    def diet(self):  # Here diet, walf functions don't have implementations
        pass 

    def walk(self):
        pass 

    def behavior(self):
        print('They show complex facial expression and social behaviour.')


chimpanze = Hominidae()
chimpanze.behavior()

class Human(Hominidae):

    def diet(self):
        print("Humans are omnivorous.")
    
    def walk(self):
        print("They are bipeds.")

help(ABC)

'''

'''
class Hominidae(ABC):

    @abstractmethod  #This decarator
    def diet(self):  # Here diet, walf functions don't have implementations
        pass 

    def walk(self):
        pass 

    def behavior(self):
        print('They show complex facial expression and social behaviour.')

#we can't create object as methods don't have implementations...even in derieved class if it don't have implementations

'''