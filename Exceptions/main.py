from exceptions import CustomError1, CustomError2, CustomError3
# try - except
# POO -> inheritance -> Exception -> BaseException

try:
    numbers = [0,1,2,3,4,5]
    number1 = numbers[0]
    number2 = numbers[10]

    result = number1 / number2

    #print('The operation result is:', result)
    #print('The program has fisnished')

#except ZeroDivisionError as error:
#    print('sorry, this operation have to next errors:', error)

#except NameError as error:
#    print('sorry, this operation have to next errors:', error)

#except IndexError as error:
#    print('sorry, this operation have to next errors:', error)

except Exception as error:
    print('sorry, this operation have to next errors:', error)

else:
    print('The operation result is:', result)
finally:
    print('The program has fisnished')



def validate_username(username):
    if username == 'cody':
        raise Exception('The username cant to be cody')

    if len(username) < 6:
        raise Exception('The username havent a len older than six')
    return True

try:
    result = validate_username('cody')
    print(result)
except Exception as error:
    print(error)


# Exceptions uniques
# POO

class UsernameCodyException(Exception):

    def __init__(self):
        self.message = 'The username cant to be cody.'
        super().__init__(self.message)

class UsernameLenException(Exception):

    def __init__(self, username):
        self.message = f'The username: {username} cant have a len order or equal to six'

def validate_username(username):
    if username == 'cody0':
        raise UsernameCodyException()

    if len(username) < 6:
        raise UsernameLenException(username)
    return True

try:
    result = validate_username('cody')
    print(result)
except UsernameCodyException as error:
    print(error)
except UsernameLenException as error:
    print('The username lenght is not valide')
except Exception as error:
    print('Sorry')

#-----------Group Exceptions uniques----------------
try:
    raise ExceptionGroup(
        'Un grupo de errores propios.',
        [CustomError1(), CustomError2(), CustomError3()]
    )
#except ExceptionGroup as group:
#    print(group)

except *CustomError1:
    print('Error type 1')

except *CustomError2:
    print('Error type 2')

except *CustomError3:
    print('Error type 3')

#----------------------------------------
class UsernameException(Exception):

    def __init__(self):
        super().__init__('the username is not valide.')

    def is_valid_to_raise(self):
        return len(self.__notes__) > 0

    def show_notes(self):
        for note in self.__notes__:
            print(">>>", note)

def username_validation(username):

    username_error = UsernameException()

    if len(username) <= 5:
        username_error.add_note('the lenght to be older to five.')

    if username.lower() == 'cody':
        username_error.add_note('The username cant to be cody')

    if '@' in username:
        username_error.add_note('The signe @ cant find in the username.')

    if username_error.is_valid_to_raise():
        raise username_error

    return True

try:
    username = 'Cody'
    username_validation(username)
except UsernameException as error:
    print(error)
    error.show_notes()

