'''
Photos details here
'''



from datetime import datetime
from main import Photo, Photographer


p1 = Photo(1, "Camera", 2.2, "Camera is for memory" )
p2 = Photo(2, "Drome", 5.2, "Flying Camera" )
p3 = Photo(3, "Stand", 2.5, "Camera holder")
p4 = Photo(4, "DSLR", 10.2, "Big Camera")
p5 = Photo(5, "Webcam", 10.25, "Computer Camera")
p6 = Photo(6, " Digital Camera", 15.3, "Old Style CAmera")
p7 = Photo(7, "REd Camera", 50.3, "Camera for high quality photo")
p8 = Photo(8, "Lens", 5, "DSLR Image")
p9 = Photo(9, "Wiper", 1.1, "Used for cleaning Cameras")
p10 = Photo(10, "Spary", 0.5, "Spraying cleaner" )


ram = Photographer(1, "Ram", 2, [p1,p2], "REEV", datetime.now(), "ram@gmail.com")
shyam = Photographer(2, "Shyam", 2, [p1,p2], "REEV", datetime.now(), "shyam@gmail.com")
# for photo in ram.photos:
#     pr90int(photo)


ram.photographer_details()
shyam.photographer_details()
# ram.photo_desc()