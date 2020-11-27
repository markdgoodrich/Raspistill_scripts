# Pi Photography 
-------------

A simple collection of python scripts for photography and video recording projects.

This system uses [RaspberryPi](https://www.raspberrypi.org/), the [Raspberry Pi High Quality Camera](https://www.raspberrypi.org/products/raspberry-pi-high-quality-camera/?resellerType=home), and [C-mount Lenses](https://thepihut.com/products/raspberry-pi-high-quality-camera-lens).

Photo resolution is set at 4056x3040.
Video resolution is set at 1920x1080.

All photos are saved to the Apache Web server default directory.  This allows users on the same network to view the photos easily.  Instructions on how to install Apache are below.

When recording videos, the programs will ask if the user is using an external USB.  If 'No', then the videos are saved to the default Video direction '/home/pi/Videos/'.  If "Yes", you will need to enter the name of the USB device.


## Scripts
* DurationRecord.py - Records a video of a certain length, given in seconds.
* Interval.py - Takes a photo at a certain interval for a specified duration, set by the user.
* PhotoBooth.py - A photobooth-style application that runs constantly; it will provide a preview and snap a picture when the button is pressed.
* Preview.py - Displays the current camera view for 15 seconds.  No video or photograph is recorded.  Useful for getting objects in focus.
* RecordVideo.py - Records a video until the user tells it to stop.
* TakePhoto.py - Takes a single photo.


Running the scripts
---------------
To run any of the scripts, simple open the terminal, navigate to the directory, and type:
```
python3 *NameOfTheScript*
```
So taking a photo would simply be:
```
python3 TakePhoto.py
```

Setting up Apache
----------------------
All photos are saved to the Apache Web server default directory.  This allows users on the same network to view the photos easily.

To install Apache on the Raspberry Pi, type the following command into the Terminal:
```
sudo apt update
```

Then install Apache with this:
```
sudo apt install apache2 -y
```

The apache directory '/var/www/html' should now be present.  Any users on the network can type in the IP Address of the Pi into their browsers to see your photographs.




