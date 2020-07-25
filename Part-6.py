import pygame
import os

pygame.init()
win = pygame.display.set_mode((1000, 500))

# Load Images of the Character
stationary = pygame.image.load(os.path.join("Sprites/Hero", "standing.png"))
#One way to do it - using the sprites that face left.
left =  [pygame.image.load(os.path.join("Sprites/Hero", "L1.png")),
         pygame.image.load(os.path.join("Sprites/Hero", "L2.png")),
         pygame.image.load(os.path.join("Sprites/Hero", "L3.png")),
         pygame.image.load(os.path.join("Sprites/Hero", "L4.png")),
         pygame.image.load(os.path.join("Sprites/Hero", "L5.png")),
         pygame.image.load(os.path.join("Sprites/Hero", "L6.png")),
         pygame.image.load(os.path.join("Sprites/Hero", "L7.png")),
         pygame.image.load(os.path.join("Sprites/Hero", "L8.png"))
         ]
#Another (faster) way to do it - using the sprites that face right
right = [None]*9
for picIndex in range(0,8):
    right[picIndex] = pygame.image.load(os.path.join("Sprites/Hero", "R" + str(picIndex+1) + ".png"))
    picIndex+=1

# Load Background
bg_pic = pygame.image.load('desert_BG.png')
bg = pygame.transform.scale(bg_pic, (1000, 500))

x = 250
y = 390
velx = 8
move_right = False
move_left = False
stepIndex = 0

# Draw Game
def draw_game():
    global stepIndex

    win.blit(bg, (0, 0))

    if stepIndex+1 >= 17:
        stepIndex = 0
    if move_left:
        win.blit(left[stepIndex//2], (x, y))
        stepIndex+=1
    elif move_right:
        win.blit(right[stepIndex//2], (x, y))
        stepIndex += 1
    else:
        win.blit(stationary, (x, y))

# Movement
def movement():
    userInput = pygame.key.get_pressed()

    global x, y, move_right, move_left
    if userInput[pygame.K_RIGHT]:
        x += velx
        move_right = True
        move_left = False
    elif userInput[pygame.K_LEFT]:
        x -= velx
        move_left = True
        move_right = False
    else:
        move_left = False
        move_right = False
        stepIndex = 0

#Mainloop
run = True
while run:

    movement()
    draw_game()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.time.delay(30)
    pygame.display.update()





