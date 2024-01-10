'''
This is Login utilities which helps to verify user before login
'''
from .file_io import file_reader, file_list_writer


def login(username,password):
    status = False
    users = file_reader("data/users.csv")
    for user in users:
        if username.strip() == str(user.split(',')[1].strip()):  
            if password.strip() == user.split(',')[2].strip():
                print(password, user.split(',')[2].strip())
                #new_user = f"{user.split(',')[0]},{user.split(',')[1]},{user.split(',')[2]},{user.split(',')[3]}\n"
                print("Login successful")
                status = True
        else:
            
            status = False
    file_list_writer('data/users.csv', users)
    
    return status