'''
1. there are two ways of representing rectangular areas
1)a tuple of four integers: (x, y, width, height)
2)a pygame.Rect object

2.a list of all the attributes of pygame.Rect object
Attribute Name     Description
myRect.left        the int value of the x coordinate of the left side of the rectangle
myRect.right       the int value of the x coordinate of the right side of the rectangle
myRect.top         the int value of the y coordinate of the top side of the rectangle
myRect.bottom      the int value of the y coordinate of the bottom side of the rectangle
myRect.centerx     the int value of the x coordinate of the center of the rectangle
myRect.centery     the int value of the y coordinate of the center of the rectangle
myRect.width       the int value of the width of the rectangle
myRect.height      the int value of the height of the rectangle
myRect.size        a tuple of two integers, the width and height of the rectangle
myRect.topleft     a tuple of two ints: (left, top)
myRect.topright    a tuple of two ints: (right, top)
myRect.bottomleft  a tuple of two ints: (left, bottom)
myRect.bottomright a tuple of two ints: (right, bottom)
myRect.midtop      a tuple of two ints: (centerx, top)
myRect.midbottom   a tuple of two ints: (centerx, bottom)
myRect.midleft     a tuple of two ints: (left, centery)
myRect.midright    a tuple of two ints: (right, centery)
'''

import pygame
import sys

pygame.init() 

window_size = (800, 600) 
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Pygame Rectangule Example")

spamRect = pygame.Rect(10, 20, 200, 300)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # fill the screen with a background
    screen.fill((255, 128, 128, 0.5))
    
    #draw the rectangle with red color
    pygame.draw.rect(screen,(0,255,0), spamRect)
    
    #update the display
    pygame.display.flip() 

pygame.quit()
sys.exit()