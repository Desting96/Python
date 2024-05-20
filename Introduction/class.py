"""
Class Rules
1. checks if the attribute exists within the object
2. checks if the attribute exists within the class - read
3. throw error
"""
class Cars: #Parenct Class
    color = ""
    brand = ""
    year = 0
    countrycar = ""

    def __init__(self, color, brand, year, countrycar):
        self.color = color
        self.brand = brand
        self.year = year
        self.countrycar = countrycar


class Person(Cars): #Son Class
    name = ""
    years = 0
    country = ""

person = Person("green", "Mustang", 2006, "España")

person.name = "Carlos"
person.country = "Bogota"

print(person.countrycar)
print(person.name)

print(person.__dict__) #Dictionary


#----------------------------
class User:
    username = ''
    email = ''

    def __init__(self, username = '', email = ''):
        self.username = username
        self.email = email

user = User()
user1 = User('User','email')

print(user.__dict__)
print(user1.__dict__)

"""Inheritance"""
class Mascota: #Parent Class
    def eat(self):
        print('The pet eats.')
    
    def sleep(self):
        print('The pet is sleeps')

class Perro(Mascota):
    pass

class Gato(Mascota):
    pass

duke = Perro()
duke.eat()
duke.sleep()

patricio = Gato()
patricio.eat()
patricio.sleep()

"""Multiple Inheritance"""
class Animal():
    def eat(self):
        print('The pet eats.')

    def sleep(self):
        print('The pet is sleeps')

class Mascota(Animal): #Parent Class
    pass

class Felino:
    def hunt(self):
        print('El felino caza.')

class Gato(Mascota, Felino):
    pass

patricio = Gato()
patricio.eat()
patricio.sleep()
patricio.hunt()

"""Method overloading"""
class Living:
    def sleep(self):
        print('The being sleep.')

class Animal(Living):
    def eat(self):
        print('The pet eats.')

    def sleep(self):
        print('The pet sleeps')

class Pet(Animal): #Parent Class

    def eat(self):
        super().eat()
        print('The animal eats')

class Feline:
    def hunt(self):
        print('El feline hunting.')

class Cat(Pet, Feline):

    def __init__(self, name):
        self.name = name

    def eat(self):
        super().eat()
        print(f'{self.name} eats.')

    def sleep(self):
        print(f'{self.name} sleeps')

patricio = Cat('Patricio')
patricio.eat()
patricio.sleep()
patricio.hunt()

"""Class Attribute"""

class Circle:

    pi = 3.141592

    @classmethod
    def area(cls, radio):
        return cls.pi * (radio ** 2)

result = Circle.area(14)
print(result)