from datetime import datetime
import os
from picamera import PiCamera
import time

#Take a photo
#name it
#add it to/var/www/html/

camera = PiCamera()
camera.resolution = (4056,3040)
path = "/var/www/html/Interval_" + datetime.now().strftime('%Y%m%d') + "_" + datetime.now().strftime('%H:%M')

#check to see fi directory arleady exists
if os.path.exists(path):
    pass
else:
    os.mkdir(path)
    #IF it doesn't exist, make it.

interval = int(input("Time between pictures (in seconds): "))
time_span = int(input("For how long (in minutes): "))
counter = int((time_span*60)/interval)

#camera.capture(path + '/1.jpg')
#Now, how to increment this?

for i in range(counter):
    picture_name = path + '/%s.jpg' %i
    camera.capture(picture_name)
    time.sleep(interval)
    

