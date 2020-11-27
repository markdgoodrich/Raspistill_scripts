from datetime import datetime
import os
import subprocess
#Take a photo
#name it
#add it to/var/www/html/

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


#ISO
iso = input("Enter ISO (100-800): ")
while int(iso) < 100 or int(iso) > 800:
    print("ISO out of range.  Select an ISO between 100 and 800.")
    iso = input("Enter ISO (100-800): ")

#shutter speed
ss_input = input("Enter Shutter Speed, in seconds (1/60, 3, etc): ")
if '/' in ss_input:    #if it is a fraction
    num, den = ss_input.split('/')
    ss = (int(num)/int(den))*10**6 #Converts time to microseconds
else:
    ss = int(ss_input)*10**6 #Converts time to microseconds

wb_options = ['off', 'auto', 'sun', 'clod', 'shade', 'tungsten', 'fluorescent', 'incandescent', 'flash', 'horizon']
wb_input = input('Pick your White Balance.  Press "Enter" to default to off.  Press "H" to see options: ')
if wb_input.upper() == 'H':
    print(wb_options)
    wb_input = input('Pick your White Balance.  Press "Enter" to default to off.  Press "H" to see options: ')
elif wb_input.lower() in wb_options:
    wb = wb_input.lower()
elif wb_input == '':
    wb = "off"
else:
    print("Invalid selection. Press 'H' to see options, or 'Enter' to default to no white balance.")


subprocess.run(["raspistill", "-r", "-ss", str(ss), "-ISO", iso, "-awb", wb, "-o", picture_name])