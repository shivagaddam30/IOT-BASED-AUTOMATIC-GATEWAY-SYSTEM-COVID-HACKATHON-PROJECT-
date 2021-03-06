import RPi.GPIO as GPIO
import time
import os

sensor = 16
GPIO.setmode(GPIO.BOARD)

GPIO.setup(3 , GPIO.OUT)
GPIO.setup(sensor,GPIO.IN)
p = GPIO.PWM(3, 50)

p.start(0)

def check():
    file = open('/C:/Users/shiva gaddam/Desktop/code/check.txt.txt')
    val = file.read()
    file.close()
    return val

def plate():
    file = open('/C:/Users/shiva gaddam/Desktop/code/plate.txt')
    plate = file.read()
    file.close()
    return plate

def openw():
    p.ChangeDutyCycle(7.5) # turn towards 180 degree
    print('opening gate...')
    time.sleep(3)
    p.ChangeDutyCycle(2.5)
    time.sleep(1) # sleep 1 second

try:
    cnt = 0
    while (cnt < 1):
        if GPIO.input(sensor):
            print ('Object detected')
            os.system('raspistill -o /C:/Users/shiva gaddam/Desktop/code/images/image1.jpg -q 100 -sh 20') # command to capture image through Pi camera directely
            print ('taking photo')
            os.system('python3 /C:/Users/shiva gaddam/Desktop/code/imgpr.py')
            print('number plate extrating...')
            os.system('python3 /C:/Users/shiva gaddam/Desktop/code/data_extract.py')
            print('Number plate : ',plate())
            val = check()
            print('check value:', val)
            if(val == 'OK'):
                print('Open')
                openw()
            else:
                print('un registered....')
            cnt = cnt + 1
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()