import pygame

pygame.init() # initialise pygame

win = pygame.display.set_mode((500, 500))   #width and height of window
                                            # that our game is displayed in.
pygame.display.set_caption("First Game")

radius = 20
x = 250
y = 300
velx = 5
vely = 10
jump = False
m = 1

run = True
while run:
    win.fill((0, 0, 0))                     # fill surface with black color

    for event in pygame.event.get():        #this code allows us to
        if event.type == pygame.QUIT:       #quit game
            run = False

    userInput = pygame.key.get_pressed()

    if userInput[pygame.K_LEFT]:
        x -= velx
    if userInput[pygame.K_RIGHT]:
        x += velx


    if jump == False and userInput[pygame.K_SPACE]:
        jump = True

    if jump:
        y -= 0.5*m*(vely**2)
        vely -= 1
        if vely<0:
            m = -1
        if vely < -10:
            jump = False
            m = 1
            vely = 10

    pygame.time.delay(30)                   #to make sure things don't happen instantly


    pygame.draw.circle(win, (255,255,255), (int(x),int(y)), radius)
    pygame.display.update()
