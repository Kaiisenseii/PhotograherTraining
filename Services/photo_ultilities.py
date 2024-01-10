'''
this is photo utilities which helps to view, add, delete, update  photos in .csv
'''
from tabulate import tabulate
from Services.file_io import file_reader, file_appender, file_list_writer
from Models.photos import get_last_id_photos

def get_all_photos():
    '''
    helps to view all the photos
    '''
    photos = file_reader("data/photos.csv")
    data = []
    for photo in photos:
        data.append([photo.split(',')[0],photo.split(',')[1],photo.split(',')[2],photo.split(',')[3]])    
    print(tabulate(data))

def add_new_photo():
    '''
    helps to add new photos
    '''
    photo_id = get_last_id_photos() + 1
    name = input("Enter the name of the photo:\n")
    location = input("Enter the loation where you photoshooted: \n")
    photo_alt = input("Write any description of the given photo:\n")
    
    new_photo= (f"{photo_id}, {name}, {location}, {photo_alt}\n")
    file_appender("data/photos.csv", new_photo)
    print("New photo successfully added.")

def delete_existing_photos():
    '''
    helps to delete existing photos
    '''
    photo_id = input("Enter id: \n")
    photos = file_reader("data/photos.csv")
    for photo in photos:
        if str(photo.split(',')[0]) == str(photo_id):
            photos.remove(photo)
        file_list_writer("data/photos.csv", photos)
    print("************************************")
    print("Photographers Removed Successfully")
    print("************************************")
             
def update_photos():
    '''
    helps to update existing photos in .csv 
    '''
    photo_id = input("Enter id: \n")
    photos = file_reader("data/photos.csv")
    for photo in photos:
        if str(photo.split(',')[0]) == str(photo_id):
            photos.remove(photo)
            name=input(f"Enter the new name for {photo.split(',')[1]} : ")
            location=input(f"Enter the new price for {photo.split(',')[2]} : ")
            photo_alt=input(f"Enter the new category for {photo.split(',')[3]} : ")
            photos.append(f"{id}, {name},{location},{photo_alt}")
    file_list_writer("data/products.csv",photos)