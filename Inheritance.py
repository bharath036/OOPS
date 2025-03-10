
#Sub classes are inherited from parent class
'''
class Shape:

    def __init__(self,shape_type):
        self.__type = shape_type

    def get_type(self):
        return self.__type
    
circle = Shape('circle')
type(circle)
'''

class Shape:

    def __init__(self,shape_type,color='Red'):
        self.__type = shape_type 
        self.__color = color

    def get_type(self):
        return self.__type 
    
    def get_color(self):
        return self.__color
    
    def get_area(self):
        pass

    def get_perimeter(self):
        pass 

s = Shape('cicle')
s.get_area()
s.get_perimeter()
'''
#Actually for different shapes , attributes are different and formulas are different
#Here shape the base class or parent class or super class
#Child class is refered as child class or sub class or derived calass
class Circle(Shape):
    pass 
#Below throws error
#cirle = Circle() #Circle is a shape. Cicle class invokes the __init__() method defined in shape

circle = Circle('circle') #this is correct
print(type(circle))

class Square(Shape):
    pass 

square = Square('square')
print(type(square))
'''
'''

class Circle(Shape):

    def __init__(self):
        Shape.__init__(self,'circle')

class Square(Shape):

    def __init__(self):
        Shape.__init__(self,'square')

circle = Circle()
square = Square()

print(type(circle),type(square))

print(circle.get_type())
print(square.get_type())

'''
'''
#Defining implementations of Base Class Methods
import math
class Circle(Shape):

    def __init__(self,radius):
        Shape.__init__(self,'circle')
        self.__radius = radius

    def get_area(self):
        return math.pi*self.__radius*self.__radius
    def get_perimeter(self):
        return 2*math.pi*self.__radius*self.__radius
    
c1 = Circle(11)
print(c1.get_area())
'''

#Super class and sub class hierachey
#Defining methods in the sub class
#super().__init(name,prize) Reference the parent of the current child class

#Module entity?
#Multiple Inheritance
#A class that derives from multiple base classes
#Inherit attributes from all its base classes
'''
class Father:
    pass 

class Mother:
    pass 
class Child1(Father,Mother):
    pass 

print(help(Child1))

#Now the base class order changes as we given mother father
#print help function and see the changes
class Child2(Mother, Father):
    pass 
print(help(Child2))
'''
'''
class Father:
    def heigth(self):
        print('I have inherited my height from my father')

class Mother:
    def intelligence(self):
        print('I have inherited my intelligence from my mother')

class Child(Father, Mother):

    def experience(self):
        print("My own experiences")

c =Child()
c.heigth()
c.intelligence()

'''
'''
class Employee:
    def __init__(self,name,age):
        self.__name = name 
        self.__age = age 

    def show_name(self):
        print(self.__name)

    def show_age(self):
        print(self.__age)


class Salary:
    def __init__(self,salary):
        self.__salary = salary 
    
    def get_salary(self):
        print(self.__salary)

class Database(Employee,Salary):

    def __init__(self,name,age,salary):
        Employee.__init__(self,name,age)
        Salary.__init__(self,salary)

emp1 = Database('robin',26,99000)
emp1.show_name()
emp1.show_age()
#To know method resolution order
print(help(Database))

'''

#Multilevel Inheritance
'''
class Grandparent:

    def height(self):
        print('I have inherited my height from my grandparent')

class Parent(Grandparent):

    def intelligence(self):
        print('I have inherited my intelligence from my Parent')

class Child(Parent):

    def experience(self):
        print('My experience are all my own')

print(help(Child))

c = Child()
c.height()
'''
'''
#What is object here and why we are passing
class Grandparent(object):

    def __init__(self,city):
        self.__city = city 
    
    def get_city(self):
        return self.__city 

class Parent(Grandparent):

    def __init__(self,city,lastname):
        Grandparent.__init__(self,city)
        self.__lastname = lastname

    def get_lastname(self):
        return self.__lastname

p1 = Parent(city = 'Vja',lastname='smith')
print(p1.get_city())

#for multilevel we improve the class for example
'''
'''
class Person(Parent):

    def __init__(self,city,lastname,firstname):
        Parent.__init__(self,city,lastname)
        self.__firstname = firstname

    def get_firstname(self):
        return self.__firstname

person1 = Person('kentucky','mark','smith')
print(person1.get_lastname())
'''
'''
#CHECK FOR SUPER() KEYWORD
class Person(Parent):

    def __init__(self,city,lastname,firstname):
        Parent.__init__(self,city,lastname)
        self.__firstname = firstname

    def get_firstname(self):
        return self.__firstname

    def get_introduction(self):
        lastname = super().get_lastname()
        city = super().get_city()

        print('Hi I am %s %s from %s' %(self.__firstname,lastname,city))

    def get_information(self):
        lastname = self.get_lastname()  #here super() keyword is not used 
        city = self.get_city()

        print('Hi I am %s %s from %s' %(self.__firstname,lastname,city))

p = Person('Kentucky','john','lily')

p.get_information()

'''


#Polymorphism
#The ability of an object to take many forms
'''
class Hominidae():
    def communication(self):
        print('They use auditory calls and visual cues.')

    def walk(self):
        print("They are knuckle-walkers, used to hand and swing from one tree to another.")

class Human(Hominidae):

    def communication(self):
        print('They use language to communicate.')

    def walk(self):
        print('They are bipeds.')

class Gorilla(Hominidae):

    def communication(self):
        print('They use 25 distinct vocalizations to communicate.')

    def walk(self):
        print('They are knuckle-walkers.')

#Let's create 3 objects
hominidae_1 = Hominidae()
human_1 = Human()
gorilla_1 = Gorilla()

#If we call respected function codes are executed in the respected classes
hominidae_1.communication()
human_1.communication()
gorilla_1.communication()

'''

'''
class BankAccount:

    def __init__(self,balance):
        self.__balance = balance 

    def deposit(self,value):
        self.__balance = self.__balance + value 

        print('Deposit value:',value)
        print('Balance after depositing:',self.__balance)

    def withdrawl(self,value):
        self.__balance = self.__balance - value 

        print('Withdrawl amount :',value)
        print('Balance after withdrawl: ', self.__balance)

b_1 = BankAccount(1500)
b_1.deposit(500)

b_1.withdrawl(200)

#Here this class exibits polymorphism
class CurrentAccount(BankAccount):

    def __init__(self,balance):
        super().__init__(balance)

    def withdrawl(self, value):
        if value>10000:
            print('Contact your branch manager')
        else:
            super().withdrawl(value)

c_1 = CurrentAccount(1500)
c_1.withdrawl(500)

class SavingsAccount(BankAccount):

    def __init__(self, balance):
        super().__init__(balance)
    
    def  deposit(self,value):
        value += 0.05*value 
        super().deposit(value)

s_1 = SavingsAccount(2000)
s_1.deposit(500)

'''

