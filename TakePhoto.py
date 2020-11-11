from datetime import datetime
import os
from picamera import PiCamera

#Take a photo
#name it
#add it to/var/www/html/

camera = PiCamera()
camera.resolution = (4056,3040)
path = "/var/www/html/" + datetime.now().strftime('%Y%m%d')

#check to see fi directory arleady exists
if os.path.exists(path):
    pass
else:
    os.mkdir(path)
    #IF it doesn't exist, make it.

#camera.capture(path + '/1.jpg')
#Now, how to increment this?

pic_num = 1
picture_name = path + '/%s.jpg' %pic_num

while os.path.exists(picture_name):#if the file already exists....
    pic_num += 1
    picture_name = path + '/%s.jpg' %pic_num
    if os.path.exists(picture_name) == False:
        break

camera.capture(picture_name)
    
