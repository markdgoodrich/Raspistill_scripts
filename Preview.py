from datetime import datetime
import os
from picamera import PiCamera
import time


camera = PiCamera()
camera.resolution = (4056,3040)

camera.start_preview()
time.sleep(15)
camera.stop_preview()
