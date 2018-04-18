import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)


ECHO1 = 15
KNOP = 8
LASER = 10
RUN = True
START = False

GPIO.setup(ECHO1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(KNOP, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(LASER,GPIO.OUT)

def stop():
    print("stop")
    START = False
    GPIO.cleanup()

if __name__ == '__main__':
    while RUN:
        if GPIO.input(KNOP):
            START = True
        try:         
            while START:
                GPIO.output(LASER,True)
                #print( GPIO.input(ECHO1))   
                
                if GPIO.input(KNOP):
                    
                    stop()
                    break
                elif GPIO.input(ECHO1) == 0:
                    print("hit")
                else:
                    print("miss")
                time.sleep(0.5)
     
        # Reset by pressing CTRL + C
        except KeyboardInterrupt:
            stop()


