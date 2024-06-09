'''
1.rectangles, circles, ellipses, lines, or individual pixels are often called drawing primitives
2.pygame.draw.polygon(surface, color, pointlist, width)
pygame.draw.line(surface, color, start_point, end_point, width)
pygame.draw.lines(surface, color, closed, pointlist, width): if pass True to closed, the last point will be connected to the first point
pygame.draw.circle(surface, color, center_point, radius, width)
pygame.draw.ellipse(surface, color, bounding_rectangle, width): bounding_rectangle is a tuple of four integers that represent the rectangle that the ellipse will be contained in
pygame.draw.rect(surface, color, rectangle_tuple, width): rectangle_tuple is a tuple of four integers that represent the rectangle that the rectangle will be contained in
'''

import pygame, sys
from pygame.locals import *

pygame.init()

#set the window
DISPLAYSURF = pygame.display.set_mode((500, 400), 0, 32)  #set_mode((width, height), flags, depth)
pygame.display.set_caption("Drawing")

#set the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#draw on the surface object
DISPLAYSURF.fill(WHITE)  # fill is a method of the Surface object
pygame.draw.polygon(DISPLAYSURF, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106))) #draw a polygon
pygame.draw.line(DISPLAYSURF, BLUE, (60, 60), (120, 60), 4) #draw a line
pygame.draw.line(DISPLAYSURF, BLUE, (120, 60), (60, 120)) #draw a line
pygame.draw.line(DISPLAYSURF, BLUE, (60, 120), (120, 120), 4) #draw a line
pygame.draw.circle(DISPLAYSURF, BLUE, (300, 50), 20, 0) #draw a circle
pygame.draw.ellipse(DISPLAYSURF, RED, (300, 250, 40, 80), 1) #draw an ellipse
pygame.draw.rect(DISPLAYSURF, RED, (200, 150, 100, 50)) #draw a rectangle

#draw the pixel
pixObj = pygame.PixelArray(DISPLAYSURF)
pixObj[480][380] = BLACK
pixObj[482][382] = BLACK
pixObj[484][384] = BLACK
pixObj[486][386] = BLACK
pixObj[488][388] = BLACK
del pixObj

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()