"""
Input() is a function for read the data them user write in console
"""
name = input("¿What your name?\n")
"""
When you need get a data for console type integer, used the function int()
this function convert string in integer
"""
old = int(input("¿how old are you?\n"))
"""
if need convert the value in float, used function float()
"""
weight = float(input("¿How weight are you?\n"))
"""if need value or result boolean, used a operator relational"""
authorized = input("Your name is " + name + " yes/not\n") == "yes"

print("Hello", name)
print("You have", old, "old")
print("You weight", weight)
print("authorized is", authorized)
