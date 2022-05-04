import time
import ftplib
import os

from ftplib import FTP
from datetime import datetime
from gpiozero import MotionSensor
from picamera import PiCamera

import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)             # pin no. 7 (Button Mode)

print("Keeping an eye out for movement")
while True:
    i=GPIO.input(7)
    if i==0:       #motion detected

        thetime=datetime.now()
        detectiontime=thetime.strftime("%y-%m-%d-%H-%M-%S")
        extension=".jpg"
        filename=detectiontime + extension
        print("Motion Detected")
        print("Capturing Image")
        capture_command="sudo raspistill -o " + filename
        os.system(capture_command)


        print("Sending an email")
        import smtplib
        import os
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText
        from email.mime.base import MIMEBase
        from email.mime.image import MIMEImage
        from email import encoders
        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.ehlo()
        smtp.starttls()
        emailaddress='8as1931140@gmail.com'
        smtp.login('8as1931140@gmail.com', '*****rya1')
        msg=MIMEMultipart()
        img_data=open(filename, 'rb').read()
        msg['From']='8as1931140@gmail.com'
        msg['To']='8as1931140@gmail.com'
        msg['Subject']='Motion Detected'
        #msg.attach(MIMEText('Motion was detected at your house. Click <a href="myfolderpath' + 'filename' + '">here</a> to see who it was.', 'html'))
        msg.attach(MIMEImage(img_data, name=os.path.basename(filename)))
        content=msg.as_string()
        smtp.sendmail(emailaddress, emailaddress, content)
        smtp.quit()
        print("Deleting local copy of " + filename)
        os.remove(filename)
        print("Resuming Detection")


