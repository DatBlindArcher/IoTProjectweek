import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)


ECHO1 = 15
KNOP = 8
LASER = 10
RUN = True
START = False
TOGGLE = False
REDLIGHT = 12
GREENLIGHT = 7

GPIO.setup(ECHO1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(KNOP, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(LASER,GPIO.OUT)
GPIO.setup(REDLIGHT, GPIO.OUT)
GPIO.setup(GREENLIGHT, GPIO.OUT)

def stop():
    print("stop")
    global RUN
    RUN = False
    GPIO.cleanup()

def endGame():
    print("endGame")
    global START
    START = False

if __name__ == '__main__':
    try:
        while True:
            GPIO.output(LASER,True)
            if GPIO.input(ECHO1) == 0:
                GPIO.output(GREENLIGHT, False)
                GPIO.output(REDLIGHT, True)
                print("hit")
                print("---")
            else:
                GPIO.output(GREENLIGHT, True)
                GPIO.output(REDLIGHT, False)
                print("miss")

            time.sleep(0.1)

            
        """while RUN:
            #print(TOGGLE)
            if GPIO.input(KNOP):
                TOGGLE = True
            if TOGGLE:
                START = True
            #print(START)
            
            while START:
                print("inGame")
                GPIO.output(LASER,True)
                #print( GPIO.input(ECHO1))   
                time.sleep(1)
                if GPIO.input(KNOP):
                    #print("Button Pressed")
                    TOGGLE = False
                elif GPIO.input(ECHO1) == 0:
                    print("hit")
                else:
                    print("miss")
                    
                if TOGGLE == False:
                    #START = False
                    endGame()
                time.sleep(0.5)
                #print(START)
                
            time.sleep(1)"""
     
    # Reset by pressing CTRL + C
    except KeyboardInterrupt:
           stop()


