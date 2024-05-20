#Tuples
"""
The tuples are data that never change of values, they are fixed data.
The tuple are identified by have one variable y assigned data inside of '()'.
In one tuple you can used all type of data, only need separate with ','
example: name(name1,years,number, etc)
console: (name1,years,number, etc)

"""
print("tuple of data")
User = ("Carlos", 20, 25896475, 200.9)
print(User)
"""
But they can used '[]' for specific the data that is required
example: name(name1,years,number, etc)
        print(name[name1])
console: name1
"""
print(User[0])

"""
Sub-list
[start:end] new list whit start index and end index
[start:]    new list with start without end index
[:end]      new list without start with end index
[start:end:skip] new list with start index, end index and index jump
[::skip]    new list withoit start index and end index but with index jump
"""
sub_tuple = User[1:3]
sub_tuple = User[1:]
sub_tuple = User[:5]
sub_tuple = User[1:6:2]
sub_tuple = User[::2]

"""
If used a for they can iterate all the tuple and to show data by data
example: name(name1,years,number)
for element in User:
    print(element)
console: name1
         years
         number
"""
print("\n tuple iterate")
for element in User:
    print(element)


"""
Defined a function where will we return the data one people 
"""
print("\n tuple with functions")
def user():
    name = "pedro"
    years = 20
    email = "pedrocg@gmail.com"
    city = "méxico"
    return (name, years, email, city)
"""
Defined a function where iterated all data of user and print 
"""
def get_user(user):
    for data in user:
        print(data)

get_user(user())

#Listas

"""
The List are data that can change of values, they are fixed data.
The list are identified by have one variable y assigned data inside of '[]'.
"""
print("\n List of data")
User = ["Carlos", 20, 25896475, 200.9]
print(User)
"""
We can change to values of a list, only call variable and the position of value to be change
"""

User[0] = "Camilo"
print(User)
"""
If used a for they can iterated all the tuple and to show data by data
"""

print("\n List iterated")
for element in User:
    print(element)

"""
If need add values to final of the list, only need use the method append() whit the values 
example: name.append("new name")
"""
print("\n List adding news data")
User.append(25)
print(User)

"""
Used the list in a position with [position] for change the value in this position of the list
Example: name[position] = newvalue
"""
print("\n Change value position 5")
User[4] = 125.5
print(User)

"""
If need delete the ultimate value, only need use the method pop()
example: name.pop()
"""
print("\n Delete the ultimate value")
User.pop()
print(User)

"""
When need union two list in one list, used the method extend()
example name.extend(name2)
"""
print("\n Union of two List")
Car = ["porsche", "paid out"]
print(Car)
User.extend(Car)
print(User)

"""
If need delete a value in a position an specific, used the function del and after
the name of the list with the position to remove
Example: del list[position]
"""

print("\n Delete value position 4")
print(User)
del User[3]
print(User)

"""
if need delete an item in specific, used the method remove()
and inside of '()' place the element to remove, this method only remove
the first element that find equal in the list 
Example: name.remove(value)
"""
print("\n Delete 25896475")
print(User)
User.remove(25896475)
print(User)

"""
count() is a method for know how many elements of a same value are in the list
"""
print("\n Number of Camilo in the list")
print(User.count("Camilo"))

"""
if need insert a value in an index specific, used the function insert 
where we put the position and the new value
"""
print("\n New value of Carlos in position 2")
User.insert(2,"Carlos")
print(User)

"""
sort() is a method for order an list of numbers
Example: name.sort()
"""

print("\n List numbers in order")
Numbers = [1, 5, 9, 5, 18, 9, 3, 6]
Numbers.sort()
Numbers.sort(reverse=True) #Invers - desc
min = min(Numbers)
max = max(Numbers)
long = len(Numbers)
print(Numbers)
res = 1 in Numbers
print(res)
res = 1 not in Numbers
print(res)
indice = Numbers.index(5)
print(indice)

"""
Sub-list
[start:end] new list whit start index and end index
[start:]    new list with start without end index
[:end]      new list without start with end index
[start:end:skip] new list with start index, end index and index jump
[::skip]    new list withoit start index and end index but with index jump
"""
print(Numbers)
sub_list = Numbers[1:3]
sub_list = Numbers[1:]
sub_list = Numbers[:5]
sub_list = Numbers[1:6:2]
sub_list = Numbers[-3:]
print('Sublist')
print(sub_list)
"""
if need that the numbers are in order reverse, used reverse=true inside of '()' of the method sort()
Example: name.sort(reverse=true)
"""

print("\n List numbers in order reverse")
Numbers.sort(reverse=True)
print(Numbers)

"""
If you need to move back by the list, you only need to change the number of the position
of positive a negative
Example: print(name[-5])
"""

print("\n data position 2 in moved back")
print(User[-2])

"""
if need remove all element, used de function clear()
"""
User.clear()
print(len(User))

#Generate tuple of a list
names = ['Calor','Pedro','Juan']
names_tuple = tuple(names)
print(names_tuple)
print(type(names_tuple))

#Generate list of a tuple
lastNames = ('Perez','Gonzales','Hurtado')
lastNames_list = list(lastNames)
print(lastNames)
print(type(lastNames_list))

#Unpacked
"""
Assign values of truple in variables
Skip value with *_ or only _
Group list *
"""
numeros = (1,2,3,4,5,6,7,8,9,10)
one, two, three, four, five, *otherValues = numeros

print(one)
print(two)
print(three)
print(four)
print(five)
print(otherValues)

#Skip 6,7,8
one, two, three, four, five, *otherValues, nine, ten = numeros

print(nine)
print(ten)
print(otherValues)

#Skip 2,6,7,8
one, _, three, four, five, *_, nine, ten = numeros

print(one)
print(three)
print(four)
print(nine)
print(ten)

#Packed
numbre_list = [1,2,3,4,5,6,7]
number_tuple = (10,20,30,40,50)
number_list2 = [100,200,300,400,500]
number_tuple2 = (1000,2000,3000,4000,5000)

result = zip(numbre_list,number_tuple,number_list2,number_tuple2)
result = tuple(result)
print(result)
