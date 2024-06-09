import pygame

pygame.init()

color1 = pygame.Color(255, 0, 0) # red
color2 = pygame.Color(255, 0, 0, 128) # red with alpha

print("color1: ", color1)
print("color2: ", color2)

is_equal = (color2 == (255, 0, 0, 128))
is_equal2 = (color1 == color2)
print("color2 == (255, 0, 0, 128): ", is_equal)
print("color1 == color2: ", is_equal2)

pygame.quit()

#the output will be shown in the terminal