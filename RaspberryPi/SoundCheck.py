def playSound(filename):
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

import pygame
#import os
import time

#os.system('mpg123 /home/pi/Desktop/music.mp3')
pygame.init()
playSound('/home/pi/Desktop/music.mp3')
while pygame.mixer.music.get_busy():
    print("Song is playing")
    time.sleep(1)
print("Finished")
#print(str(pygame.mixer.music.get_volume()))

"""
load
play
stop
rewind
pause
unpause
fadeout
set_volume
get_volume
play(loops=X)
"""
