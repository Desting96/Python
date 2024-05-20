#Generate a list from a String
lenguages = 'Python Ruby Java Rust C++ C'
lenguagesWithCharacter = 'Python-Ruby-Java-Rust-C++-C'

lenguages_list = lenguages.split()
lenguagesWithCharacter_list = lenguagesWithCharacter.split('-')
lenguagesWithCharacter_list_onlyTwo = lenguagesWithCharacter.split('-',2)

print(lenguages_list)
print(lenguagesWithCharacter_list)
print(lenguagesWithCharacter_list_onlyTwo)

#Generate a String from a list

lenguajes = ['Python','Ruby', 'Java', 'Rust']
string_lenguages = ' '.join(lenguages)
print(string_lenguages)
print(type(string_lenguages))

#Concat String

name = 'Eduardo Ismael'
last_name = 'Garcia'

name_complete = 'Mr. ' + name + ' ' + last_name + ' Perez' + '.'
print(name_complete)

name_complete = 'Mr. %s %s %s.' %(name,last_name,'Perez')
print(name_complete)

name_complete = 'Mr. {} {} {}.' .format(name,last_name,'Perez')#placeholders
print(name_complete)

name_complete = 'Mr. {name} {surname} {second_surname}.' .format(
    name = name,
    surname = last_name,
    second_surname = 'Perez')#placeholders
print(name_complete)

# fString Interpolation
name_complete = f'Mr. {name} {last_name} {"Perez."} {10 * 20}'
print(name_complete)

#Function Print
print(name,last_name,'Perez', 1.89) #All value are separate by default by a space 
print(name,last_name,'Perez', 1.89, sep='-') #Separate print by -

#Validate subString
title = 'Print the information'
count_string = title.count('o')
print(count_string)

print('print' in title)

print('print' in title.lower())

print(title.startswith("Print"))

print(title.endswith('mation'))

"""
ljust -> justify to left
rjust -> justify to right
center -> center
"""
message = 'Hello world!'
message_left = message.ljust(20)
print(message_left + '.')
message_right = message.rjust(20)
print(message_right + '.')
message_center = message.center(20)
print(message_center)