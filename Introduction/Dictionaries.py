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
"""
print(Users.values())
print(Users.keys())
"""
If you need a values specific, you can used the method get() and inside specific the key
"""
print(Users.get("name"))
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
