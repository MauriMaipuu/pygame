import pygame

pygame.init()

screen = pygame.display.set_mode([640, 480])  # teeme ekraani kus hakkab m2ng jooksma
pygame.display.set_caption("Yes")


bg = pygame.image.load('imgs/bg_rally.jpg')  # anname m2ngule tausta
screen.blit(bg, [0, 0])

sinine = pygame.image.load('imgs/f1_blue.png')  #
screen.blit(sinine, [160, 0])

pygame.display.flip


if timr.timr() % 10 == 0:
    blusepeed +=1


run = True  #lisame funktsiooni et m2ngu saaks ristist kinni panna
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()