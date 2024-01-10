'''
Contains Photographers class which describes what details the Photographers have during Registration
'''


from Services.file_io import file_reader

# class Photographers:
#     '''
#     creates class Photographers
#     '''
#     def __init__(self, id, name, price, equipment):
#         self.id = id
#         self.name = name
#         self.price = price
#         self.equipment = equipment
#     def print_info(self):
#         '''
#         changes to string dunder/magic method
#         '''
#         print(f"Name: {self.name},  Price: {self.price}, Equipment: {self.equipment}")
#         return self
    
#     def __str__(self):
#         return f"Name: {self.name}, Price: {self.price}, Equipment:{self.equipment}"

def get_last_id():
    '''
    contains get_last_id method which helps to give id to the database of Photographers registered
    '''
    photographers = file_reader("data/photographers.csv")
    if photographers[-1].split(',')[0] == 'ID': 
        return 0
    return int(photographers[-1].split(',')[0])
    