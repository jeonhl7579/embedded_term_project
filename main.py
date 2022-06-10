import RPi.GPIO as GPIO
import time
import picamera
import datetime

pirPin=16

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pirPin,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

camera = picamera.PiCamera()
camera.resolution=(1024,768)

try:
    while True:
        sensorValue=GPIO.input(pirPin)
        if sensorValue==1:
            now=datetime.datetime.now()
            print(now)
            fileName=now.strftime(' %Y-%m-%d %H:%M:%S ')
            camera.capture('/home/pi/project/images' + fileName + '.jpg')
            time.sleep(5)
        print(sensorValue)
        time.sleep(1)
except KeyboardInterrupt:
    pass

GPIO.cleanup()