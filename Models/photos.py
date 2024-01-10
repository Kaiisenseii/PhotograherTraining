'''

Contains Photo class which describes what details the Photo have during Registration




'''

from Services.file_io import file_reader

# class Photos:
#     def __init__(self, id, name, location, photo_alt):
#         self.id = id
#         self.name = name
#         self.location = location
#         self.photo_alt = photo_alt
#     def print_photo_info(self):
#         '''
        
#         '''
#         print(f"Name: {self.name},  Location of Photo: {self.location}, PhotoDescription: {self.photo_alt}")
#         return self
    
#     def __str__(self):
#         return (f"Name: {self.name}, Location of Photo: {self.location}, PhotoDescription: {self.photo_alt}")

def get_last_id_photos():
    '''
        contains get_last_id method which helps to give id to the database of Photographers registered
    '''
    
    photos = file_reader("data/photos.csv")
    if photos[-1].split(',')[0] == 'ID':
        return 0
    return int(photos[-1].split(',')[0])
    