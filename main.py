'''
Creating Photographer class 
'''


class Photographer:
    def __init__(self,id, name="", age= 0, photos= list(), company='', date='', email=""):
        self.id = id
        self.name = name
        # self.age = age
        
        
        self.age = age if self.validate_age(age) else 0
        
        # if self.validate_photos(photos):
        #     print("Photographer created with valid data")
        #     self.photos = photos
        # else:
        #     print("Invalid Invalid photo inserted")
        #     self.photos = list()
            
        self.photos = photos if self.validate_photos(photos) else list()

        self.email = email if self.validate_email(email) else "Unvalidated Email"
            
        self.company = company
        self.date = date if self.validate_date(date) else "Unvalida Date"
        
          
    def photo_desc(self):
        print(f"\nPhotos of photographer {self.name} are:")
        for i, ele in enumerate(self.photos):
            print("ID: ", ele.id)
            print ("Name: ", ele.photo_name)
            print("Size of Image: ", ele.size)
            print(f"Alt Text of Photo of {ele.photo_name}: ", ele.alt_text)
            print()
        
    def photographer_details(self):
        print(f""" 
PHOTOGRAPHER INFORMATION:::  
Name : {self.name}
Age : {self.age} 
Company :{self.company}
Joined Date:{self.date}
Email ID : {self.email}
..............................................
              """)
        self.photo_desc()

        print("........................................")
    

    def validate_age(self, _age):
        return True if (_age < 10) and (_age > 10) else False
        # if (_age<10) and (_age>100):
        #     return True
        # else:
        #     return False
        
    def validate_email(self, _email):
        return True if isinstance(_email,str) and (("@" in _email) and ("." in _email) and (_email.endswith(".com"))) else False
        # if isinstance(_email, str):
        #     if (("@" in _email) and ("." in _email) and (_email.endswith(".com"))): return True
        #     else: return False
        # return False
    
    def validate_date(self, _date):
        return True if isinstance(_date, str) else False
        
    def validate_photos(self, _photos):
        status = False
        if isinstance(_photos, list):
            for _photo in _photos:
                status = False
                if isinstance(_photo, Photo):
                    status = True
                else:
                    status = False
            
        return status
                      
           
              
              
    def __str__(self) -> str:
        return str(self.name)
  
        
class Photo:
    def __init__(self,id, photo_name='', size=0.0, alt_text=''):
        self.id= id
        self.photo_name = str(photo_name)
        self.size = float(size)
        self.alt_text = alt_text
        
        
        
    def __str__(self) -> str:
        return str(self.photo_name)
