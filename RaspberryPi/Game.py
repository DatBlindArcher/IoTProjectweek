import RPi.GPIO as GPIO
import time
import requests

ECHO1 = 15
KNOP = 8
LASER = 10
RUN = True
START = False
TOGGLE = False
SCORE = 0

GPIO.setmode(GPIO.BOARD)
GPIO.setup(ECHO1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(KNOP, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(LASER,GPIO.OUT)

def stop():
    print("stop")
    global RUN
    RUN = False
    GPIO.cleanup()

def endGame():
    print("endGame")
    global START
    global SCORE
    START = False

    #Send SCORE To robbe his Server
    response = requests.get('http://193.191.176.129:8080/createplayer')
    player = response.json()
    player['score'] = SCORE
    response = requests.post('http://193.191.176.129:8080/setplayer', json = player)
    print(response.json())
    SCORE = 0

def showScore(hit):
    global SCORE
    if hit:
        SCORE = SCORE + 10
    else:
        SCORE = SCORE - 5

    if SCORE < 0:
        SCORE = 0

    print(str(SCORE))

if __name__ == '__main__':
    try: 
        while RUN:
            GPIO.output(LASER,False)
            #print(TOGGLE)
            if GPIO.input(KNOP):
                print("Button Pressed")
                TOGGLE = True
                time.sleep(3)
            if TOGGLE:
                START = True
                GPIO.output(LASER,True)
                
                print("3")   
                time.sleep(1)
                print("2")   
                time.sleep(1)
                print("1")   
                time.sleep(1)
            #print(START)
            
            while START:
                print("inGame")
                
                
                if GPIO.input(KNOP):
                    print("Button Pressed")
                    TOGGLE = False
                    time.sleep(3)
                #elif GPIO.input(ECHO1) == 1:
                    #print("hit")
                else:
                    showScore(GPIO.input(ECHO1))
                    #print("miss")
                    
                if TOGGLE == False:
                    #START = False
                    endGame()
                time.sleep(0.1)
                #print(START)
                
            time.sleep(1)
     
    # Reset by pressing CTRL + C
    except KeyboardInterrupt:
           stop()


