from picamera import PiCamera
camera = PiCamera()

import RPi.GPIO as GPIO
import time
from time import sleep

# camera.start_preview()
# sleep(5)
# camera.stop_preview()
# 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
Ena, In1,In2 =9,16,12
EnaL, In1L,In2L =15,27,22
Tri, Echo= 14,17
GPIO.setup(Ena, GPIO.OUT)
GPIO.setup(In1, GPIO.OUT)
GPIO.setup(In2, GPIO.OUT)
GPIO.setup(EnaL, GPIO.OUT)
GPIO.setup(In1L, GPIO.OUT)
GPIO.setup(In2L, GPIO.OUT)

GPIO.setup(Tri, GPIO.OUT)
GPIO.setup(Echo, GPIO.IN)

pwm=GPIO.PWM(Ena,100)
pwm.start(0)
pwmL=GPIO.PWM(EnaL,100)
pwmL.start(0)

while True:
  
    GPIO.output(Tri,False)
    print("waiting for sensor to settle")
    sleep(0.2)
    GPIO.output(Tri,True)
    sleep(0.00001)
    GPIO.output(Tri,False)
    while GPIO.input(Echo)==0:
        pulse_start=time.time()
    while GPIO.input(Echo)==1:
        pulse_end=time.time()
    pulse_duration=pulse_end-pulse_start
    distance=pulse_duration*17150
    distance=round(distance,2)
    print("distance:",distance,"cm")
    sleep(2)
    
    if (distance>100):
        GPIO.output(In1,GPIO.LOW)
        GPIO.output(In2,GPIO.HIGH)  
        pwm.ChangeDutyCycle(50)
        
        GPIO.output(In1L,GPIO.LOW)
        GPIO.output(In2L,GPIO.HIGH)  
        pwmL.ChangeDutyCycle(50)
        sleep(2)
    
    elif (distance <=100):
        pwm.ChangeDutyCycle(0)
        pwmL.ChangeDutyCycle(0)
        sleep(2)
    