import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

TRIG = 8
ECHO1 = 16
ECHO2 = 18


LAMPEN = [22,23,21,19,13,11,12,10,7,5,40] #40=5 5=3

for i in range(0,11):
    GPIO.setup(LAMPEN[i], GPIO.OUT)
    
KNOP = 15
RUN = True

TIME_PLAYED = 0

GPIO.setup(KNOP, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO1, GPIO.IN)
GPIO.setup(ECHO2, GPIO.IN)

score = 0

def stop():
    print("stop")
    RUN = False
    GPIO.cleanup()
	
def getTime(trig, echo):
    # set Trigger to HIGH
    GPIO.output(trig, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
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

def showScore(hit1, hit2, punten):
        
    if hit1 and hit2:
        punten = punten + 1
    else:
        punten = punten - 1
        
    if punten > 10:
        punten = 10
    if punten < 0:
        punten = 0
        
    for i in range(0,punten+1):
        GPIO.output(LAMPEN[i],True)
    
    for i in range(punten, 11):
        GPIO.output(LAMPEN[i], False)
        
    return punten

if __name__ == '__main__':
    try:
        print("start")
        
        while RUN:
            time1 = getTime(TRIG, ECHO1)
            time2 = getTime(TRIG, ECHO2)
            
            hit = time1 < 0.002
            hit2 = time2 < 0.002
            
            score = showScore(hit, hit2, score)
            
            print(score)

            time.sleep(1)
            
            if GPIO.input(KNOP):
                stop()
                break
 
    # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        stop()
        
