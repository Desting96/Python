#Silence errors
try:
    raise Exception('its not possible to continue.')
except Exception as error:
    pass
finally:
    print('Finally program')


from contextlib import suppress

with suppress(Exception):
    result = 10 / 0 
    print(result)

print('Finally program')