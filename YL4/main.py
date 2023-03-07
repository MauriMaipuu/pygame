#Mauri Maipuu
import pygame
import random
import sys
import time
# Imporditakse moodulid

pygame.init()  #pygame moodul
screen = pygame.display.set_mode((640, 480))  #ekraani suurus
pygame.display.set_caption("Ralli - Mauri")  #akna tiitel

clock = pygame.time.Clock()  #Loodakse clock

startTime = time.time()  #Stardiaeg
score = 0  #skoor

bg = pygame.image.load("../YL4/imgs/bg_rally.jpg")  #Taust 1
bg2 = pygame.image.load("../YL4/imgs/bg_rally.jpg")  #Taust 2 animatsioon
bgposX = 0  #taust1 X positsioon
bg2posX = 480  #taust2 X positsioon
bgspeedX = -3  #tausta animatsiooni kiirus

f1Blue = pygame.image.load("../YL4/imgs/f1_blue.png")  #sinise autu pilt
f1Blue = pygame.transform.rotate(f1Blue, 180)  #sinise autu teistpidi

f1Blue2 = pygame.image.load("../YL4/imgs/f1_blue.png")  #autu2 pilt
f1Blue2 = pygame.transform.rotate(f1Blue2, 180)  #autu2 teistpidi

f1Red = pygame.image.load("../YL4/imgs/f1_red.png")  #autu punane pilt

gameover = False  #game over muutuja

blueSpeedY = 3  # sinise autukiirus

bluePosY = random.randint(0, 100)  #sinise autu positsioon Y
blue2PosY = random.randint(0, 100)  #sinise autu2 positsioon Y
redPosX, redPosY = 298, 390  #punase autu positsioonid
redSpeedY = 0  #punase auto kiirus Y
bluePosX = random.randint(300, 460)  #sinise auto positsioon X
blue2PosX = random.randint(130, 280)  #sinise auto positsioon X

while not gameover:  #korratakse kuni gameover on false
    clock.tick(120)  #kaadrisagedus

    for event in pygame.event.get():  #loop et mäng töötaks
        if event.type == pygame.QUIT:  #kui aken pannakse kinno
            sys.exit()  # lõpetatakse mäng

    #lisatakse taustapildid
    screen.blit(bg, (0, bgposX))
    screen.blit(bg2, (0, bg2posX))

    #kiirused
    bgposX -= bgspeedX
    bg2posX -= bgspeedX

    #taustapildi loop
    if bgposX >= 480:
        bgposX = -480
    if bg2posX >= 480:
        bg2posX = -480

    #lisatakse sinised autod
    screen.blit(f1Blue, (bluePosX, bluePosY))
    screen.blit(f1Blue2, (blue2PosX, blue2PosY))

    #liigutatakse autosi
    bluePosY += blueSpeedY + 0.8
    blue2PosY += blueSpeedY + 1

    #lisatakse punane auto
    screen.blit(f1Red, (redPosX, redPosY))
    redPosY += redSpeedY  # auto liigutamine

    #kuvatakse skoor
    screen.blit(pygame.font.Font(None, 30).render(f"Skoor: {score}", True, [255, 255, 255]), [0, 0])

    #autode positsiooni taastamine
    if bluePosY >= 480:  #auto lõpus
        bluePosY = -120  #auto positsiooni taastamine
        score += 1 #suurendame skoori
        bluePosX = random.randint(130, 280)  #auto panek suvakasse kohta
    if blue2PosY >= 480:  #auto 2 lõpus
        blue2PosY = -120  # taastame tema positsiooni
        score += 1  # suurendame skoori
        blue2PosX = random.randint(300, 480)  #auto panek suvalisse kohta

    if redPosY >= 480:  #punane auto pole ekraanil näha
        redPosY = -120  #taastame ta positsiooni

    #punase auto liigutamine
    key = pygame.key.get_pressed()  #vajutatud klahv all
    if key[pygame.K_LEFT]:  #kui vasak klahvall
        redPosX -= 5  # liigutatakse autot vasakule
    if key[pygame.K_RIGHT]:  # kui parem klahv all
        redPosX += 5  # liigutatakse autot paremale

    #mängu lõpp, kui sinine auto puudutab punast
    if redPosY + 55 >= bluePosY >= redPosY - 55:  #kui sinine ja punane auto panevad y-koordinaadil kokku
        if redPosX + 50 >= bluePosX >= redPosX - 50:  #kui sinine ja punane auto panevad x-koordinaadil kokku
            gameover = True  #lõpetatakse mäng

    if redPosY + 55 >= bluePosY >= redPosY - 55:  #kui sinine ja punane auto panevad y-koordinaadil kokku
        if redPosX + 50 >= bluePosX >= redPosX - 50:  #kui sinine ja punane auto panevad x-koordinaadil kokku
            gameover = True  #lõpetatakse mäng

    #suurendakse kiirust iga minuti tagant
    if time.time() % 60 == 0:  #aeg jagatakse 60-ga
        blueSpeedY += 1  #suurendakse kiirust 1 võtta

    #kuvame aega
    screen.blit(pygame.font.Font(None, 20).render(f"Aeg: {int(time.time() - startTime)}",
                                                  True, [255, 255, 255]), [0, 20])
    pygame.display.flip()  #värskendatakse ekraani

while True:  #lõppematu kordus, et kontrollida kas mäng on läbi
    if gameover:  #kui mäng on läbi
        # kuvatakse "Mäng läbi!"
        screen.blit(pygame.font.Font(None, 50).render("Mäng läbi!", True, [255, 255, 255]), [230, 300])
        # kuvatakse skoori
        screen.blit(pygame.font.Font(None, 50).render(f"Skoor: {score}", True, [255, 255, 255]),
                    [240, 200])
        pygame.display.flip()  # uuendatakse ekraani

    for event in pygame.event.get():  #ootatakse sündmust
        if event.type == pygame.QUIT:  #kui ekraan suletakse
            sys.exit()   #lõpetatakse mäng
