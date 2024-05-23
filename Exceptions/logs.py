# Logging
import logging
import traceback
import contextlib

#INFO       = 10
#DEBUG      = 20
#WARNING    = 30
#ERROR      = 40
#CRITICAL   = 50

logging.basicConfig(level = logging.ERROR,  #default level is 30
                    filename = 'errors.log',#type a
                    format="%(asctime)s:%(levelname)s:%(message)s") 

"""logging.info('Hello, this is a message info')
logging.debug('Hello, this is a message debug')
logging.warning('Hello, this is a message warning')
logging.error('Hello, this is a message error')
logging.critical('Hello, this is a message critical')"""

#---------------------------------------------------------
'''def write_on_log_error(error):
    exception_info = {
        'message': str(error),
        'detail': traceback.format_exc()
    }
    logging.error(str(exception_info))

try:
    10 / 0

except Exception as error:
    write_on_log_error(error)
'''
#--------------------------------------------------
@contextlib.contextmanager
def write_on_log_error():
    try:
        yield
    except Exception as error:
        exception_info = {
            'message': str(error),
            'detail': traceback.format_exc()
        }
        logging.error(str(exception_info))


with write_on_log_error():
    #result = 10 / 0
    #print(result)
    file = open('users.txt')