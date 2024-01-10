'''
it is photographers utilities which helps to view, add, delete, update photographers
'''
from tabulate import tabulate
from Models.photographers import get_last_id
from .file_io import file_reader, file_appender, file_list_writer


def gell_all_photographers():
    '''
    helps to view all the photographers
    '''
    photographers = file_reader('data/photographers.csv')
    # print(photographers)
    data = []
    for photographer in photographers:
        data.append([photographer.split(',')[0], photographer.split(',')[1], photographer.split(',')[2], photographer.split(',')[3]])
    
    print(tabulate(data))

   
def add_new_photographers():
    '''
    helps to add new photographers
    '''
    photographer_id = get_last_id( ) + 1
    name = input("Enter your name: \n")
    price = float(input("Enter the price for events: \n"))
    equipment = str(input("Enter what is your main equipment: \n"))
    
    new_photographers = f"{photographer_id}, {name}, {price}, {equipment} \n"
    file_appender("data/photographers.csv", new_photographers)
    print("*************************************")
    print("Added Successfully")
    print("*************************************")
   
def delete_existing_photographers():
    '''
    helps to delete photographers
    '''
    photographer_id = input("Enter id: \n")
    photographers = file_reader("data/photographers.csv")
    for photographer in photographers:
        if str(photographer.split(',')[0]) == str(photographer_id):
            photographers.remove(photographer)
        file_list_writer("data/photographers.csv", photographers)
    print("************************************")
    print("Photographers Removed Successfully")
    print("************************************")
             
def update_photographer():
    '''
    helps to update photographers
    '''
    photographer_id = input("Enter id: \n")
    photographers = file_reader("data/photographers.csv")
    for photographer in photographers:
        if str(photographer.split(',')[0]) == str(photographer_id):
            photographers.remove(photographer)
            name = input(f"Enter the new name for {photographer.split(',')[1]} : ")
            price = input(f"Enter the new price for {photographer.split(',')[2]} : ")
            equipment = input(f"Enter the new category for {photographer.split(',')[3]} : ")
            photographers.append(f"{photographer_id}, {name},{price},{equipment}\n")
            print(photographers)
    
    file_list_writer("data/photographers.csv",photographers)
    print("************************************")
    print("Photographers Updated Successfully")
    print("************************************")