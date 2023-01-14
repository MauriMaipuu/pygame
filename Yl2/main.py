import pygame
from pygame import draw
import sys
import subprocess

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Test m2ng")
screen.fill([240, 105, 210])

bg = pygame.image.load("img/background.png")
screen.blit(bg, [0, 0])

chrt = pygame.image.load("img/robot-preview.png")
screen.blit(chrt, [0, 235])

chat = pygame.image.load("img/chat.png")
chat = pygame.transform.scale(chat, [350, 350])
screen.blit(chat, [110, 80])

font = pygame.font.Font(pygame.font.match_font('segoeui'), 52)
font.set_bold(True)
text = font.render("Tere, mina", True, [0, 0, 0])
text_width = text.get_rect().width
text_height = text.get_rect().height
screen.blit(text, [155, 140])

font = pygame.font.Font(pygame.font.match_font('segoeui'), 52)
font.set_bold(True)
text = font.render("olen Fery", True, [0, 0, 0])
text_width = text.get_rect().width
text_height = text.get_rect().height
screen.blit(text, [165, 185])

pygame.display.flip()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
