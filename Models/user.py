'''

Contains User class which describes what details the are needed to have during during Registration


'''


from Services.file_io import file_reader


# class User:
#     def __init__(self, id, username, email, password):
#         self.id = id
#         self.username = username
#         self.email = email
#         self.password = password
        
    
#     def __repr__(self):
#         return f"{self.id}, {self.username}, {self.email}, {self.password}"
    
#     def __str__(self):
#         return f"{self.id}, {self.username}, {self.email}, {self.password}"
    
    
def get_last_id():
    '''
    contains get_last_id method which helps to give id to the database of Photographers registered
    '''
    users = file_reader("data/users.csv")
    if users[-1].split(',')[0].strip() == 'ID':
        return 0
    else:
        return int(users[-1].split(',')[0])