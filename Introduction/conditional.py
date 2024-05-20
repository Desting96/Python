"""
#In this program we will see all the conditional for python
#that can be perform and receive values for console.

#This program compare three numbers and sample the number major,
#intermediate and minor among them
"""

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the three number: "))

if (num1 >= num2) and (num1 >= num3):
    major = num1
    if num2 > num3:
        inter = num2
        minor = num3
    else:
        inter = num3
        minor = num2
elif num2 > num3:
    major = num2
    if num1 > num3:
        inter = num1
        minor = num3
    else:
        inter = num3
        minor = num1
else:
    major = num3
    inter = num2
    minor = num1

print("The number major is: {} \nThe number intermediate is: {} \nThe number minor is: {}".format(major, inter, minor))

result = 10
color = 'Verde' if result >= 7 else 'Rojo'
print(result,color)

'''
The while is a operation for repetitions of actions
 many times depending of the condition assigned
'''
inc = 0
while inc < 5:
    print(inc)
    inc = inc + 1


'''
The foreach is an operation to execute an itarable element
'''
usuarios = ['usuario1','usuario2','usuario3','usuario4']
for usuario in usuarios:
    print(usuario)

'''
The break-continue are operation than function for stop and continue a ciclo for or while
'''
titulo = 'operation break-continue'
for character in titulo:
    if character == ' ':
        break
    if character == 'p':
        continue
    print(character)

'''
A call is defined show(), which we will make a for with which 
we will use the range function that will allow to pass 3 parameter,
range(a, b, c), where a is the beginning, b the end and c the hops of the loop
example: range (0,5,2)
console: 0 2 4
'''

def show():
    for i in range(0, 20, 2):
        print(i)

show()

"""Values empty"""
result = None
print(result)
print(type(result))

"""Values true/false"""
"""
False
None
0
0.0
'' / ""
[]
()
{}
"""
