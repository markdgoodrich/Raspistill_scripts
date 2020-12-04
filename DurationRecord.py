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

duration = int(input("How long to film (in seconds): "))
camera.start_preview()

video_name = path + '.h264' 



camera.start_recording(video_name)
sleep(duration)
camera.stop_recording()
camera.stop_preview()
print("Video recording finished.")

