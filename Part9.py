import pygame
import os

# Init and Create Window (win)
pygame.init()
win_height = 400
win_width = 800
win = pygame.display.set_mode((win_width, win_height))

# Load and Size Images
stationary = pygame.image.load(os.path.join("Hero", "standing.png"))
left = [pygame.image.load(os.path.join("Hero", "L1.png")),
        pygame.image.load(os.path.join("Hero", "L2.png")),
        pygame.image.load(os.path.join("Hero", "L3.png")),
        pygame.image.load(os.path.join("Hero", "L4.png")),
        pygame.image.load(os.path.join("Hero", "L5.png")),
        pygame.image.load(os.path.join("Hero", "L6.png")),
        pygame.image.load(os.path.join("Hero", "L7.png")),
        pygame.image.load(os.path.join("Hero", "L8.png")),
        pygame.image.load(os.path.join("Hero", "L9.png"))
        ]
right =[pygame.image.load(os.path.join("Hero", "R1.png")),
        pygame.image.load(os.path.join("Hero", "R2.png")),
        pygame.image.load(os.path.join("Hero", "R3.png")),
        pygame.image.load(os.path.join("Hero", "R4.png")),
        pygame.image.load(os.path.join("Hero", "R5.png")),
        pygame.image.load(os.path.join("Hero", "R6.png")),
        pygame.image.load(os.path.join("Hero", "R7.png")),
        pygame.image.load(os.path.join("Hero", "R8.png")),
        pygame.image.load(os.path.join("Hero", "R9.png"))
        ]
bullet_img = pygame.transform.scale(pygame.image.load(os.path.join("Bullets", "bullet.png")), (10, 10))
background = pygame.transform.scale(pygame.image.load('desert_BG.png'), (win_width, win_height))

class Hero:
    def __init__(self, x, y):
        # Walk
        self.x = x
        self.y = y
        self.velx = 10
        self.vely = 10
        self.face_right = True
        self.face_left = False
        self.stepIndex = 0
        # Jump
        self.jump = False
        # Bullet
        self.bullets = []
        self.cool_down_count = 0

    def move_hero(self, userInput):
        if userInput[pygame.K_RIGHT] and self.x <= win_width - 62:
            self.x += self.velx
            self.face_right = True
            self.face_left = False
        elif userInput[pygame.K_LEFT] and self.x >= 0:
            self.x -= self.velx
            self.face_right = False
            self.face_left = True
        else:
            self.stepIndex = 0

    def draw(self, win):
        if self.stepIndex >= 9:
            self.stepIndex = 0
        if self.face_left:
            win.blit(left[self.stepIndex], (self.x, self.y))
            self.stepIndex += 1
        if self.face_right:
            win.blit(right[self.stepIndex], (self.x, self.y))
            self.stepIndex += 1

    def jump_motion(self, userInput):
        if userInput[pygame.K_SPACE] and self.jump is False:
            self.jump = True
        if self.jump:
            self.y -= self.vely*4
            self.vely -= 1
        if self.vely < -10:
            self.jump = False
            self.vely = 10

    def direction(self):
        if self.face_right:
            return 1
        if self.face_left:
            return -1

    def cooldown(self):
        if self.cool_down_count >= 20:
            self.cool_down_count = 0
        elif self.cool_down_count > 0:
            self.cool_down_count += 1

    def shoot(self):
        self.cooldown()
        if (userInput[pygame.K_f] and self.cool_down_count == 0):
            bullet = Bullet(self.x, self.y, self.direction())
            self.bullets.append(bullet)
            self.cool_down_count = 1
        for bullet in self.bullets:
            bullet.move()
            if bullet.off_screen():
                self.bullets.remove(bullet)


class Bullet:
    def __init__(self, x, y, direction):
        self.x = x + 15
        self.y = y + 25
        self.direction = direction

    def draw_bullet(self):
        win.blit(bullet_img, (self.x, self.y))

    def move(self):
        if self.direction == 1:
            self.x += 15
        if self.direction == -1:
            self.x -= 15

    def off_screen(self):
        return not(self.x >= 0 and self.x <= win_width)

# Draw Game
def draw_game():
    win.fill((0, 0, 0))
    win.blit(background, (0,0))
    player.draw(win)
    for bullet in player.bullets:
        bullet.draw_bullet()
    pygame.time.delay(30)
    pygame.display.update()

# Instance of Hero-Class
player = Hero(250, 290)

# Mainloop
run = True
while run:

    # Quit Game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Input
    userInput = pygame.key.get_pressed()

    # Shoot
    player.shoot()

    # Movement
    player.move_hero(userInput)
    player.jump_motion(userInput)

    # Draw Game in Window
    draw_game()
