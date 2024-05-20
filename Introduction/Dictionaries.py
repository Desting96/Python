"""
The dictionaries are blocks and they the present by '{}' , inside every block is
represented by two elements, one key and one value, separated by ':' and with ','
separated every block
Example: name = {key1:value1, key2:value2,.......}
And inside the values you can have tuple, list, numbers, strings, all types of data
"""
Users = {"name": "Carlos", "surname": "Perez", "years": 20}
"""
values() is a method that return all values that has the dictionaries
keys() is a method that return all keys that has the dictionaries
items() is a method that return all in a duple
"""
print(Users.values())
print(Users.keys())
print(Users.items())
"""
If you need a values specific, you can used the method get() and inside specific the key
"""
print(Users.get("name"))
print(Users.get('some', 'The key no exist in dictionary'))
"""
clear() is a method for empty the dictionaries
copy() is a method for copied the block of a dictionaries in other dictionaries
"""
UsersCopy = Users.copy()
print(UsersCopy)
Users.clear()
print(Users)
"""
update() is a method for update the dictionaries, you can add a new block placing 
other key or change the value of a block, placing the same key
"""
UserNewData = {"name": "Andres"}
UsersCopy.update(UserNewData)
print(UsersCopy)

"""if need add element in a dictionary, yu can uses variable[name_key] = value"""
elements = {}

elements['name'] = 'cody' #if the key does not exist, create the key and it's value
elements[(1,2,3)] = 'the key is a truple'
print(elements)
elements['name'] = 'code' #if a key exists, change the value than these keys have
print(elements)

"""Get the value of a key"""
dictionary = {'a': 1, 'b':2, 'c':3, 'd' :4}
print('z' in dictionary)
value = dictionary['d']
print(value)
value = dictionary.setdefault('e', 5) #if the value doesnt exist, add and return the value but no error
print(value)
print(dictionary)

"""Delete element"""
dictionary = {'a': 1, 'b':2, 'c':3, 'd' :4}
print(len(dictionary))

del dictionary['a'] # Delete element wiht key a
valor = dictionary.pop('b') # Delete element wiht key b

print(valor)

print(dictionary)

print(len(dictionary))

dictionary.clear() #Delete all elements

print(dictionary)
