import pygame  # impordime pygame

pygame.init()

screen = pygame.display.set_mode([640, 480])  # teeme ekraani kus hakkab m2ng jooksma
pygame.display.set_caption("Yes")
screen.fill([234, 105, 241])

bg = pygame.image.load('img/bg_shop.jpg')  # anname m2ngule tausta
screen.blit(bg, [0, 0])

seller = pygame.image.load('img/seller.png')  # lisame poemyya
seller = pygame.transform.scale(seller, [250, 300])  # teeme 6ige suuruseks
screen.blit(seller, [60, 150])

cht = pygame.image.load('img/chat3.png')  # lisame r22kimis kasti
cht = pygame.transform.scale(cht, [250, 200])
screen.blit(cht, [200, 75])

font = pygame.font.Font(pygame.font.match_font('Arial'), 25)  # lisame r22kimis kasti teksti
text = font.render("Tere, olen Mauri", True, [255, 255, 255])

text_width = text.get_rect().width  # teksti suuruse 6igeks tegemine
text_height = text.get_rect().height

screen.blit(text, [225, 150])

vykk = pygame.image.load('img/VIKK logo.png')  # lisame vikki logo
vykk = pygame.transform.scale(vykk, [300, 50])
screen.blit(vykk, [0, 0])

cake = pygame.image.load('img/cake.png')  # lisame koogi
cake = pygame.transform.scale(cake, [100, 100])
screen.blit(cake, [436, 200])

swrd = pygame.image.load('img/Mõõk.png')  # lisame m66ga
swrd = pygame.transform.smoothscale(swrd, [40.3, 36.8])
screen.blit(swrd, [390, 325])

pygame.draw.line(screen, [255, 255, 255], [2, 2], [295, 2], 1)  # teeme vikkilogole ymber valge kasti
pygame.draw.line(screen, [255, 255, 255], [2, 50], [295, 50], 1)

pygame.draw.line(screen, [255, 255, 255], [2, 2], [2, 50], 1)
pygame.draw.line(screen, [255, 255, 255], [265, 2], [265, 50], 1)
pygame.draw.arc(screen, [255, 255, 255], [260, 2, 50, 50], -3.14 / 3, 2)

pygame.display.flip

run = True  #lisame funktsiooni et m2ngu saaks ristist kinni panna
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
