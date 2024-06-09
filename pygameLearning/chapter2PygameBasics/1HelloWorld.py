#chapter2: pygame Basics
'''
1.
GUI: Graphical User Interface(show a window with images and colors)
CLI: Command Line Interface
2. source code for helloworld
3. all of the pygame functions dealing with graphics, sound and other features that pygame provides are in the pygame module
4. a main game loop normally contains the following:
    - event handling
    - game logic(udpate game state)
    - drawing(visual representation of the game state)
5.pixel coordinates:
    - (0,0) is the top-left corner of the window
6.Surface Objects: represent a rectangular 2D image
in particular, the surface object returned by the pygame.display.set_mode() is called the display surface
7.common color
aqua rgb(0,255,255)
black rgb(0,0,0)
blue rgb(0,0,255)
fuchsia rgb(255,0,255)
gray rgb(128,128,128)
green rgb(0,128,0)
lime rgb(0,255,0)
maroon rgb(128,0,0)
navy blue rgb(0,0,128)
olive rgb(128,128,0)
purple rgb(128,0,128)
red rgb(255,0,0)
silver rgb(192,192,192)
teal rgb(0,128,128)
white rgb(255,255,255)
yellow rgb(255,255,0)
8.transparent colors:
1)alpha value: 0 is fully transparent(invisible), 255 is fully opaque
half transparent green color: rgb(0, 255, 0, 128)
2)in order to use transparent colors, we should create a Surface object with the convert_alpha() method
anotherSurface = DISPLAYSURF.convert_alpha()
invisible pink unicorn rgb(255, 192, 192, 0)
'''
import pygame, sys  
from pygame.locals import *

pygame.init()
DISPLAYURL = pygame.display.set_mode((400,300))
pygame.display.set_caption("Hello World!")
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    