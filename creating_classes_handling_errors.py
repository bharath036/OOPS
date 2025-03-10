#creating classes
'''
class Dog:
    pass 

print(type(Dog))
dog_1 = Dog()
print(dog_1)
dog_2 = Dog()
print(dog_2)

#properties can be added in the below way
dog_1.kind = 'Dachshud'
dog_1.life_expetancy = '12-16 years'
dog_2.kind = 'Labrador Retriever'

print(dir(dog_1))  #the propertied diffined will be seen in the bottom
'''

'''
class Dog:
    #class variables
    kind = ''
    age = 0
    name = ''
    vaccinated = False

dog_1 = Dog()
print(dog_1.kind,dog_1.age,dog_1.name,dog_1.vaccinated)

#The above variables can be changed easily.
dog_1.kind = 'Golden Retriver'
print(dog_1.kind)
#if we create new instance or object, values will be default
#Every instance can define their own variables
'''

#Defining methods within python classes
'''
class Dog:
    def __init__(self):
        print('Instance initialized')
    
dog_1 = Dog()
dog_1 
'''
'''
class Dog:

    def __init__(self,kind,age,name,vaccinated = False):
        self.kind = kind 
        self.age = age 
        self.name = name 
        self.vaccinated = vaccinated

        print('instance initialized')

dog_1 = Dog('DAlmatian',3,'Rover',True)
print(dog_1)
print(dog_1.__dict__)

'''

'''
class Dog:

    def __init__(self,kind,age,name,vaccinated = False):
        self.kind = kind 
        self.age = age 
        self.name = name 
        self.vaccinated = vaccinated

        print('instance initialized')

    def get_details(self):
        return f"Name: {self.name},kind:{self.kind},Age:{self.age}"
    
dog_2 = Dog(name = 'Joe',kind = 'German sheprtd',age =4, vaccinated = True)
print(dog_2.__dict__)
print(dog_2.get_details())

print(Dog.get_details(dog_2))

'''

#Catching Exceptions Using python Try Except blocks 

#10* 2/0 zero division error
#"Hello"+3 type error 
#does_not_exist + 5 #Name error

'''
try:
    user_input = input("Please enter an integer: ")
    result = 100/ int(user_input)
    print("Here is the result, 100 divided by out input integer",result)
except ValueError:          #value and type error are related
    print("Oops an exception was thrown!")
print('Outside the try/except block')
'''
'''
try:
    user_input = input("Please enter an integer: ")
    result = 100/ int(user_input)
    print("Here is the result, 100 divided by out input integer",result)
except (ValueError,ZeroDivisionError):          #value and type error are related
    print("Oops an exception was thrown!")
print('Outside the try/except block')

'''
#lets write code based on type of error
'''
try:
    user_input = input("Please enter an integer: ")
    result = 100/ int(user_input)
    print("Here is the result, 100 divided by out input integer",result)

except ValueError as ve:          #value and type error are related
    print("Oops a value error was thrown!",ve)
    print("Error type", type(ve))

except ZeroDivisionError as zde:          #value and type error are related
    print("Oops zero division error was thrown!",zde)
    print('Error type', type(zde))

except:
    print('Well this was unexpected!')

else:
    print('Successfully executed the code in the try block!')

print('Outside the try/except block')
'''
#issubclass(ValueError,Exception)
#Both valuerror, zde are inherited by 
#Once see how can we add else and see except is not working 

#Using Finally block
#Raise an exception
#In pyhton we will raise an exception
'''
try:
    raise Exception('green','eggs','and','ham')

except Exception as exe:
    print('Exception:',exe)
    print('Typer',type(exe))
    print('arguments:',exe.args)
'''
'''
try:
    raise Exception('green','eggs','and','ham')

except Exception as exe:
    arg_1,arg_2,arg_3,arg_4 = exe.args

print(arg_1,arg_2,arg_3,arg_4)
'''

'''
def exception_raiseing_fn(switch):
    if switch == 1:
        raise ValueError('Value specified was wrong')
    elif switch == 2:
        raise NameError('Identifier not defined in the local or global scope')
    elif switch == 3:
        raise TypeError
    else:
        print('Executed without exceptions')

try:
    exception_raiseing_fn(2)

except ValueError as ve:          #value and type error are related
    print("Oops a value error was thrown!",ve)
    print("Error type", type(ve))

except NameError as ne:          #value and type error are related
    print("Oops zero Nameerror error was thrown!",ne)
    print('Error type', type(ne))

except TypeError as te:
    print('Oops a typerError was thrown',te)
    print('Error Type',type(te))

finally:
    print('Always executed. This is where you will write clean up code')

'''
#Difference between else and finally is else block is executed only if try block is executed but
#finally block is executed no matter what

