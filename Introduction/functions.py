"""The types data in python are objects """
import random

n = random.randint(1, 100)
print(n)

"""Create function"""
def summation():
    number_one = int(input('Insert the fisrt number: '))
    number_two = int(input('Insert the second number: '))

    result = number_one + number_two
    print(result)

summation()

"""Function with variables"""

def summation(n1, n2):

    result = n1 + n2
    print(result)

number_one = int(input('Insert the fisrt number: '))
number_two = int(input('Insert the second number: '))

summation(number_one, number_two)

"""Return values with functions"""
def summation(n1, n2):

    result = n1 + n2
    return result, 'The function return two values'

number_one = int(input('Insert the fisrt number: '))
number_two = int(input('Insert the second number: '))

result, message = summation(number_one, number_two)
print('The result is:',summation(number_one, number_two))
print('The result is:', result, 'message:',message)

"""Parameter Optional"""
def area_circle(ratio, pi=3.1416):
    return pi*(ratio ** 2)

print(area_circle(10))
print(area_circle(10,3.141592))
print(area_circle(pi=3.141592,ratio=10))

"""args"""
def average(*args):
    return sum(args) / len(args)

#list_num = [2,5,9,6]
#print('The average is:',average(list_num))
print('The average is:',average(2,5,9,6))

def combination(p1,p2,*args,p4):
    print(p1)
    print(p2)
    print(args)
    print(p4)

combination(10,20,1,2,3,4,5,6,7,8,p4=1000)

"""kwargs"""
def users(**kwargs): #Dictionary
    print(kwargs)
    print(type(kwargs))

users(eduardo=[10,10,8], fernando=[10,9,9])

def combination2(*args, **kwargs): #tuple and dictionary
    print(args)
    print(kwargs)

combination2(1,2,3,4,5,cody=True,curso='Python')

"""scope"""
animal = 'Lion' #Variable created global

def print_animal():
    global animal
    animal = 'whale' #Variable created local
    print(animal)
    print(id(animal))

print_animal()
print(animal)
print(id(animal))

"""Nested functions"""

def operation(amount, balance, tip='deposito'):
    def deposit(amount, balance):
        return amount + balance
    def withdrawal(amount, balance):
        if amount <= balance:
            return balance - amount
        else:
            return None

    print(deposit(10,20))
    print(withdrawal(50,20))

    if tip == 'deposito':
        return deposit(amount, balance)
    elif tip == 'retiro':
        return withdrawal(amount, balance)

print(operation(10,30,'retiro'))

"""Lambdas function"""
def centigrade_to_fahrenheit(degrees): #Normal function 
    return degrees * 1.8 + 32

print(centigrade_to_fahrenheit(10))
print(centigrade_to_fahrenheit(-1))
print(centigrade_to_fahrenheit(8))

my_function = centigrade_to_fahrenheit

print(type(my_function))
print(my_function(10))
#lambda <parameters> : body to the function
function_degrees = lambda degrees : degrees * 1.8 + 32

print(function_degrees(10))

#Lambda with parameters = lambda : true
#lambda without parameters = lambda p1=10,p2=20,p3=30 : p1+p2+p3
#lambda with asterisk = lambda *args, **kwargs : len(args) + len(kwargs)

"""Callbacks"""
averagep = lambda *args : sum(args) / len(args)
approved = lambda qualification : qualification >= 7
print(averagep(10,10,9,8,7))
print(approved(7))

def is_approved(qualification) :
    return qualification >= 90

def show_messages(func_average, func_approved, *args):
    average = func_average(*args)
    if func_approved(average):
        print(f'Felicidades, aprobaste la materia')
    else:
        print('No aprobaste la materia')

show_messages(averagep,approved,10,10,8,8,7)
show_messages(averagep,is_approved,10,10,8,8,7)

"""Closures"""
def main_function():
    a = 'a'
    b = 'b'
    def nested_function():
        nonlocal b
        c = 'c'
        b = 'change'

        print(a)
        print(b)

    nested_function()
    #print(c)

main_function()

#-------------------------------
def greet():
    def show_message():
        print('Hello')

    return show_message
response = greet()
response()

#---------------------------------
def greet(username):
    message = f'Hello {username}'
    
    def show_message():
        print(message)

    return show_message

username = "Cody"
response = greet(username)

response()

"""
Decorators
a -> The main function (Decorator)
b -> The function to decorate
c -> The decorated function
"""

def a_function(b_function):
    def c_function():
        print('>>>Beforce the call')
        b_function()
        print('>>>After the call')
    return c_function

@a_function
def greet():
    print('Hello')

greet()

@a_function
def summ():
    print(10 + 30)

summ()

#------------------------------------------------
def a_function(b_function):
    def c_function(*args, **kwargs):
        print('>>>Beforce the call')
        result = b_function(*args, **kwargs)
        print('>>>After the call')
        return result
    return c_function

@a_function
def summ(number_1, number_2):
    return number_1 + number_2

print(summ(10, 20))

"""Generators -> Lazy Literator"""
def even(): #Generator
    for number in range(0,12,2):
        #print(number)
        yield number
        print('Execution resumes')

#for par in even():
#    print(par)

generator = even()
print(next(generator))
print(next(generator))

while True:
    try:
        par = next(generator)
        print(par)
    except:
        print('The Finish generator')
        break

"""Docstring
__doc__ (Modules, class, methods and functions)
Testing ussing 'python -m doctest functions.py'
"""

def summ(number_1, number_2):
    """
    The function adds 2 enterps numbers
    Arguments:
    number_1 (int)
    number_2 (int)
    The function return the adds of the parameters.

    TODO:
        *

    >>> summ(10,20)
    30
    
    >>> summ(30,20)
    50
    """
    return number_1 + number_2

#print(summ.__doc__)
#print(help(summ))
