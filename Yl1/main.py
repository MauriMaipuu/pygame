import pygame
from pygame import draw
import sys
import subprocess

pygame.init()

GUI = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Foor - Mauri Maipuu")
GUI.fill([204, 102, 255])
pygame.draw.rect(GUI, [102, 102, 153], [110, 35, 120, 270], 0)
pygame.draw.rect(GUI, [194, 194, 214], [95, 15, 115, 270], 0)
pygame.draw.rect(GUI, [0, 0, 0], [100, 20, 105, 260], 0)
pygame.draw.circle(GUI, [255, 255, 0], [153, 150], 40, 0)
pygame.draw.circle(GUI, [255, 0, 0], [153, 65], 40, 0)
pygame.draw.circle(GUI, [0, 255, 0], [153, 235], 40, 0)

pygame.display.flip()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
