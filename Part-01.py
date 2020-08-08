import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("First Game")

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
