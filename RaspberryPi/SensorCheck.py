import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

TRIG = 8
ECHO1 = 16
ECHO2 = 18

KNOP = 15
RUN = True

GPIO.setup(KNOP, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(ECHO2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def getTime(trig, echo):
    # set Trigger to HIGH
    GPIO.output(trig, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.000001)
    GPIO.output(trig, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(echo) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(echo) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    return StopTime - StartTime

def stop():
    print("stop")
    RUN = False
    GPIO.cleanup()

if __name__ == '__main__':
    try:
        print("start")
        
        while RUN:
            time1 = getTime(TRIG, ECHO1)
            time2 = getTime(TRIG, ECHO2)
            
            hit1 = time1 > 0.0015 and time1 < 0.0020
            hit2 = time2 > 0.0015 and time2 < 0.0020
            
            if hit1 and hit2:
                print("score")
            elif hit1:
                print("hit1")
            elif hit2:
                print("hit2")
            else:
                print("no hit")
            time.sleep(1)
            
            if GPIO.input(KNOP):
                stop()
                break
 
    # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        stop()

