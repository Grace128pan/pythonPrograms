'''
1.pygame.mixer.music.load("path to the music file")
2.pygame.mixer.music.play(-1,0.0) # -1 means play the music in a loop, 0.0 means start from the beginning
if we set -1 to 1, it will play the music only once
if we set the second parameter to 10.0, it will start playing the music from 10 seconds
3.pygame.mixer.music.stop() # stop the music

'''


import pygame 
import time
import sys
from pygame.locals import *

pygame.init()
pygame.mixer.init()

sound1 = pygame.mixer.Sound("pygameLearning/chapter2PygameBasics/chicken.mp3")
sound2 = pygame.mixer.Sound("pygameLearning/chapter2PygameBasics/duck.mp3")
sound3 = pygame.mixer.Sound("pygameLearning/chapter2PygameBasics/barking.mp3")

sounds = [sound1, sound2, sound3]
current_sound_index = 0

sounds[current_sound_index].play()

window_size = (400, 300)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Playing Sounds")

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            
    time.sleep(1)
    sounds[current_sound_index].stop()
    current_sound_index = (current_sound_index + 1) % len(sounds)
    sounds[current_sound_index].play()
    
    pygame.display.flip()  # Update the display
    
pygame.quit()
sys.exit()