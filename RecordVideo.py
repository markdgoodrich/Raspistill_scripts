from datetime import datetime
import os
from picamera import PiCamera
from time import sleep
import subprocess

camera = PiCamera()
camera.resolution = (1920, 1080)

usb_answer = input("Is the external USB inserted? [Y/n]: ")
if usb_answer.upper() == "Y":
        usb_name = input("Enter the name of the USB device: ")
	path = "/media/pi/" + usb_name + "/" + datetime.now().strftime('%Y%m%d_%H%M')	
else:
	path = "/home/pi/Videos/" + datetime.now().strftime('%Y%m%d_%H:%M')

video_name = path + '.h264' 


camera.start_preview()
camera.start_recording(video_name)

print("Recording has begun!")
enter = input("	Hit ENTER to end recording.")
if enter == '':
	camera.stop_recording()
	camera.stop_preview()
print("Video recording finished.")


