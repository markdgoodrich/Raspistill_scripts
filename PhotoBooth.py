from datetime import datetime
import os
from picamera import PiCamera

#Take a photo
#name it
#add it to/var/www/html/

camera = PiCamera()
camera.resolution = (4056,3040)
path = "/var/www/html/" + datetime.now().strftime('%Y%m%d') + "_PhotoBooth"

#check to see if directory arleady exists
if os.path.exists(path):
    pass
else:
    os.mkdir(path)

pic_num = 1
picture_name = path + '/%s.jpg' %pic_num



#PhotoBooth
#Have display up
#Press 'enter' to take picture
#   Path should be 

#can change this to a button if need be.
#b=Button(14)
button = input("Hit 'Enter' to take a photo!")
camera.start_preview()

while True:
    if button == '':
        camera.capture(picture_name)
        pic_num += 1
        picture_name = path + '/%s.jpg' %pic_num
        print('Picture taken!\n')
        time.sleep(1)
