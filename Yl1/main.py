import pygame
from pygame import draw
import sys
import subprocess

pygame.init()

GUI = pygame.display.set_mode((300, 600))
pygame.display.set_caption("Foor - Mauri Maipuu")
GUI.fill([204, 102, 255])

pygame.draw.rect(GUI, [102, 102, 153], [110, 35, 120, 270], 0)

pygame.draw.rect(GUI, [194, 194, 214], [95, 15, 115, 270], 0)
pygame.draw.rect(GUI, [0, 0, 0], [100, 20, 105, 260], 0)
pygame.draw.circle(GUI, [255, 255, 0], [153, 150], 40, 0)
pygame.draw.circle(GUI, [255, 0, 0], [153, 65], 40, 0)
pygame.draw.circle(GUI, [0, 255, 0], [153, 235], 40, 0)
pygame.draw.rect(GUI, [220, 200, 214], [140, 280, 25, 270], 0)
pygame.draw.polygon(GUI, [91, 109, 125], [[148, 515], [100, 595], [200, 595], [150, 515]], 5)
pygame.draw.polygon(GUI, [0, 0, 255], [[149, 515], [134, 541.6], [165, 541.6], [149, 515]], 0)
pygame.draw.polygon(GUI, [255, 255, 255], [[119, 568.26], [102, 595], [198, 595], [181, 568.26]], 0)
pygame.draw.polygon(GUI, [0, 0, 0], [[134, 541.6], [119, 568.26], [181, 568.26], [165, 541.6]])

pygame.display.flip()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
