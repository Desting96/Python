"""variable type string"""
name = "David"
'''variable type integer'''
years = 100
'''variable type float or double'''
price = 200.2
"""
when dividing with / the result is floating
when dividing with / the result is integer
"""
print (10 / 3)
print (10 // 3)
'''variable type boolean'''
x = True
y = False
'''constants do not exist, only simulates with capitalized words'''
TITULO = 'constant variables'
'''Method for print the variables with different types to data 
    str() is a method that convert all variables to strings
    int() is a method that convert all variables to integers
    float() is a method that convert all variables to floats
'''
print("{} have {} years old and you capital is of {} usd".format(name, years, price))
print(name+" have "+str(years)+" years old and you capital is of "+str(price)+" usd")

"""
Relational operator
<
>
<=
>=
==
!=
the result is boolean
"""
print(18 > 20)

"""
Logical operator
and
or
not
the result is boolean
"""
print(True and True and 100 > 20) #Result True
print(False or False or 100 > 20) #Result True
print(True and True and 100 < 20) #Result False
print(False or False or 100 < 20) #Result False
print(not True) #Result False

"""Who do you what type of data it is?"""
valor = "Nombre"
print(type(valor)) #Return str

valor = 2
print(type(valor)) #Return int

valor = 3.1
print(type(valor)) #return float

valor = True
print(type(valor)) #Return bool
