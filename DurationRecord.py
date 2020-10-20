from datetime import datetime
import os
from picamera import PiCamera
from time import sleep
import subprocess

camera = PiCamera()
camera.resolution = (1920, 1080)

usb_answer = input("Is the external USB inserted? [Y/n]: ")
if usb_answer.upper() == "Y":
	path = "/media/pi/PiCamera/" + datetime.now().strftime('%Y%m%d_%H:%M')
	
else:
	path = "/home/pi/Videos/" + datetime.now().strftime('%Y%m%d_%H:%M')

duration = int(input("How long to film (in seconds): "))
camera.start_preview()

video_name = path + '.h264' 

#print(video_name)

camera.start_recording(video_name)
sleep(duration)
camera.stop_recording()
camera.stop_preview()
print("Video recording finished.")

#subprocess.run(["scp", video_name, "markgoodrich@192.168.0.100:/home/markgoodrich/Videos/Pi_Videos/"])


#if os.path.exists(video_name):
#	os.remove(video_name)
#else:
#	print("File does not exist")
