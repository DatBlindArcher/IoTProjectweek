import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

KNOP = 15
#LED = 5

LAMPEN = [22,23,21,19,13,11,12,10,7,5,40] #40=5 5=3

for i in range(0,11):
    GPIO.setup(LAMPEN[i], GPIO.OUT)

#GPIO.setup(LED, GPIO.OUT)
GPIO.setup(KNOP, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
    for i in range(0,11):
        GPIO.output(LAMPEN[i],GPIO.input(KNOP))
    
    print(GPIO.input(KNOP))
    time.sleep(1)

