import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Cycle")

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    pygame.display.update()