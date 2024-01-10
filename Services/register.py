'''
register new user
'''

from Models.user import get_last_id
from .file_io import file_appender

def register(username, password, email):
    '''
    helps to register new user and add to data/user.csv file
    '''
    register_id = get_last_id() + 1
    new_user= (f"{register_id}, {username}, {password}, {email}\n")
    file_appender("data/users.csv", new_user)
    