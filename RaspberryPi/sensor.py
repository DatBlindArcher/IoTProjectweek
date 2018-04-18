import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

TRIG = 12
ECHO = 16
ECHO2 = 18

LAMPG = 8
LAMPR = 10

KNOP = 3

GPIO.setup(LAMPG, GPIO.OUT)
GPIO.setup(LAMPR, GPIO.OUT)
GPIO.setup(KNOP, GPIO.IN)

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(ECHO2, GPIO.IN)
GPIO.output(TRIG, False)
GPIO.output(LAMPG, False)
GPIO.output(LAMPR, False)
run = True

while True:
    pulse_start = time.time()
    pulse_end = time.time()
    pulse_end2 = time.time()
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    """while GPIO.input(ECHO) == 0 and GPIO.input(ECHO2) == 0:
            pulse_start = time.time()
            pulse_start2 = time.time()
            
    while GPIO.input(ECHO) == 1:
            pulse_end = time.time()
            
    while GPIO.input(ECHO2) == 1:
            pulse_end2 = time.time()     """
    
    while GPIO.input(ECHO) == 0 and GPIO.input(ECHO2) == 0:
            pulse_end = time.time()
            pulse_end2 = time.time()
            
    #if GPIO.input(ECHO) == 1 and GPIO.input(ECHO2) == 1:

    pulse_duration = pulse_end - pulse_start
    #print(pulse_duration)
    pulse_duration2 = pulse_end2 - pulse_start
    #print(pulse_duration2)
    
    print(GPIO.input(KNOP)) 
    
    """if GPIO.input(KNOP):
        run = False
        print("end")"""
    
    hit = pulse_duration < 0.002
    hit2 = pulse_duration2 < 0.002
    GPIO.output(LAMPG, not hit or not hit2)
    GPIO.output(LAMPR, hit and hit2)
    time.sleep(1)

GPIO.cleanup()

 