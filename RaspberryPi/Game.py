import RPi.GPIO as GPIO
import time
#import os
import requests
import sys
import pygame

#os.system('mpg123 /home/pi/Desktop/music.mp3')

ECHO1 = 15
KNOP = 8
LASER = 10
REDLIGHT = 12
GREENLIGHT = 7
RUN = True
START = False
TOGGLE = False
AKTIF = False
SCORE = 0
BUFFER = 0

GPIO.setmode(GPIO.BOARD)
GPIO.setup(ECHO1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(KNOP, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(LASER,GPIO.OUT)
GPIO.setup(REDLIGHT, GPIO.OUT)
GPIO.setup(GREENLIGHT, GPIO.OUT)

def playSound(filename):
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play(-1)

def pauseSound():
    pygame.mixer.music.pause()

def unpause():
    pygame.mixer.music.unpause()

def stopSound():
    pygame.mixer.music.stop()

def setVolume(volume):
    pygame.mixer.music.set_volume(volume)

def getVolume():
    return pygame.mixer.music.get_volume()

def fadeOut():
    pygame.mixer.music.fadeout()

pygame.init()

def stop():
    print("[Stop]")
    fadeOut()
    global RUN
    RUN = False
    GPIO.cleanup()

def endGame():
    print("[endGame]")
    global START
    global SCORE
    global BUFFER
    global AKTIF
    AKTIF = False
    START = False
    stopSound()

    #Send SCORE To robbe his Server
    response = requests.get('http://193.191.176.129:8080/createplayer')
    player = response.json()
    player['score'] = SCORE
    response = requests.post('http://193.191.176.129:8080/setplayer', json = player)
    print(response.json())
    SCORE = 0
    BUFFER = 0
    print("Waiting for input...", end="", flush=True)

def showScore(hit):
    global SCORE
    global AKTIF
    if hit:
        GPIO.output(GREENLIGHT, True)
        GPIO.output(REDLIGHT, False)
        SCORE = SCORE + 2
        AKTIF = True
    else:
        GPIO.output(GREENLIGHT, False)
        GPIO.output(REDLIGHT, True)
        AKTIF = False
        #SCORE = SCORE - 0.5

    if SCORE < 0:
        SCORE = 0

    if SCORE % 50 == 0:
        setVolume(getVolume() + 0.1)
        print()
        print(str(getVolume()))
        print()
    #if SCORE > 22000000000000:
        #print("HACKER")

    sys.stdout.write("\rScore: " + str(SCORE)) 

    #print(str(SCORE))

if __name__ == '__main__':
    try:
        
        print("Waiting for input...", end="", flush=True)
        while RUN:
            GPIO.output(LASER,False)
            GPIO.output(GREENLIGHT, False)
            GPIO.output(REDLIGHT, False)
            #print(TOGGLE)
            if GPIO.input(KNOP):
                print("[Button Pressed]")
                TOGGLE = True
                time.sleep(3)
            if TOGGLE:
                START = True
                GPIO.output(LASER,True)
                GPIO.output(GREENLIGHT, False)
                GPIO.output(REDLIGHT, True)
                #hier stond cursor
                playSound('/home/pi/Desktop/music.mp3')
                setVolume(0.3)
                print()
                print(str(getVolume()))
                print()
                for countdown in range(5, 0, -1):
                    sys.stdout.write("\rStart in: " + str(countdown))   
                    time.sleep(1)

                sys.stdout.write("\rGo!                                 \n")
            #print(START)
            
            while START:
                #print("[inGame]")
                
                if BUFFER > 100:
                    TOGGLE = False
                
                if GPIO.input(KNOP):
                    print("[Button Pressed]")
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
                if not AKTIF:
                    pauseSound()
                    BUFFER += 1
                else:
                    unpause()
                    BUFFER = 0

                #print(START)
                
            time.sleep(1)
            print("." , end="", flush=True)
     
    # Reset by pressing CTRL + C
    except KeyboardInterrupt:
           stop()


