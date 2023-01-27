import pygame

screen = pygame.display.set_mode([640, 480])
pygame.display.set_caption("Harjutamine")

GREEN = [153, 255, 153]
RED = [255, 0, 0]
screen.fill(RED)


class Square:
    def __init__(self, color, sizea, sizeb):
        self.color = color
        self.sizea = sizea
        self.sizeb = sizeb

    def make_square(self):
        y = 1
        for i in range(35):
            x = 1
            for j in range(38):
                pygame.draw.rect(screen, self.color, [x, y, self.sizea, self.sizeb])
                x += 18
            y += 18


Square.make_square(Square(GREEN, 15, 15))

pygame.display.flip()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
