'''
THis is the menu of the program where it displays menu after login
'''

from Services.register import register
from Services.login import login
from Services.photographers_utilities import (
    gell_all_photographers, add_new_photographers, 
    delete_existing_photographers, update_photographer)
from Services.photo_ultilities import (
    get_all_photos, add_new_photo, 
    delete_existing_photos, update_photos)

def login_menu():
    '''
    first menu before login
    '''
    print("Login Menu for FreeLance Photographer")
    print()
    print("1. Login")
    print("2. Register")
    print("3. Exit")
    
    choice = int(input("Enter your choice from 1-3: "))
    if choice == 1:
        print("You selected choice 1, SO:\n")
        login_username = input("Enter your username:\n")
        login_password = input("Enter your password:\n")
        
        if login(login_username, login_password) is True:
            photo_menu()
        else:
            print("\nUsername or Password is incorrect.\n")
            login_menu()
    elif choice == 2:
        print("You selected choice 2, So:\n")
        register_username = input("Enter a new unique username:\n")
        register_password = input("Enter your password:\n")
        register_email = input("Enter your valid email address:\n")
        print(f"You Entered Username:{register_username} and Password: {register_password} and your email is {register_email}")
        register(register_username, register_password, register_email)
        login_menu()
    else:
        exit()
#first page after login
def photo_menu():
    '''
    first menu after login
    '''
    print("****************************************")
    print("Please Choose from the following menu")
    print("*************************************")
    print("1. Photographers")
    print("2. Photos")
    print("3. Change Password")
    print("4. Logout")
    
    choice= int(input("Enter your choice: \n"))
    if choice == 1:
        photographer_menu()
    elif choice == 2:
        photo_desc_menu()
    elif choice == 3:
        login_menu()
    elif choice == 4:
        login_menu()
    else: 
        print("You have entered invalid input") 

#photographers menu  
def photographer_menu():
    '''
    first menu after clicking photographers
    '''
    
    print("\n===============s==================================")
    print("Please choose from the following options from Photographers: \n")
    gell_all_photographers()
    print("\n=================================================")
    # print("1. View All Photographers ")
    print("1. Add Photographer")
    print("2. Delete Photographers") 
    print("3. Update Photographers")
    print("4. If you want to go back")
    
    
    
    choice = int(input("Enter your choice: "))
    
    # if choice == 1:
    #     gell_all_photographers()
    #     photographer_menu()
    if choice == 1:
        add_new_photographers()
    elif choice == 2:
        delete_existing_photographers()
    elif choice == 3:
        update_photographer()
    elif choice == 4:
        photo_menu()
    else: 
        print(" The choice is invalid ")
        print("===================================================")
        
#photo menu
def photo_desc_menu():
    '''
    first menu after clicking photos
    '''
    print("\n=================================================")
    print("Please choose from the following options from Photographers: \n")
    print("\n=================================================")
    print("1. View All Photos ")
    print("2. Add Photos")
    print("3. Delete Photos")
    print("4. Update Photos")
    print("5. If you want to go back")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        get_all_photos()
        photo_desc_menu()
    elif choice == 2:
        add_new_photo()
        photo_desc_menu()
    elif choice == 3:
        delete_existing_photos()
        photo_desc_menu()
    elif choice == 4:
        update_photos()
        photo_desc_menu()
    elif choice == 5:
        photo_menu()
    else: 
        print(" The choice is invalid ")
        print("===================================================")
          
        
        