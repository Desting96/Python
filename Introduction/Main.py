"""variable type string"""
name = "David"
'''variable type integer'''
years = 100
'''variable type float or double'''
price = 200.2
'''variable type boolean'''
x = True
y = False
'''Method for print the variables with different types to data 
    str() is a method that convert all variables to strings
    int() is a method that convert all variables to integers
    float() is a method that convert all variables to floats
'''
print("{} have {} years old and you capital is of {} usd".format(name, years, price))
print(name+" have "+str(years)+" years old and you capital is of "+str(price)+" usd")
