
# Home Security System
A Raspberry Pi based intruder alert system which sends the photo of the suspicious person.



## Screenshots
Raspberry Pi 3B+
![App Screenshot](https://raw.githubusercontent.com/shaurya121/Home-security-System/main/Screenshots/Rpi.jpg/468x300?text=Hello_world)
Pinout
![App Screenshot](https://raw.githubusercontent.com/shaurya121/Home-security-System/main/Screenshots/pinout.png)
Motion Sensor
![App Screenshot](https://raw.githubusercontent.com/shaurya121/Home-security-System/main/Screenshots/motion%20detector.jpg)
Idle State
![App Screenshot](https://raw.githubusercontent.com/shaurya121/Home-security-System/main/Screenshots/inactive.jpg)
When Someone Enters
![App Screenshot](https://raw.githubusercontent.com/shaurya121/Home-security-System/main/Screenshots/active.jpg)
## Installation
Update Raspberry Pi using:
```python
sudo apt-get update
sudo apt-get upgrade
```

    
## Usage/Examples
Capture the image of intruder using:
```python
capture_command="sudo raspistill -o " + filename
os.system(capture_command)
```
Now mail this image to the admin:
```python
msg.attach(MIMEImage(img_data, name=os.path.basename(filename)))
content=msg.as_string()
smtp.sendmail(emailaddress, emailaddress, content)
```
Lastly delete the local copy of image:
```python
print("Deleting local copy of " + filename)
os.remove(filename)
```

