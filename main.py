import pygame
import numpy as np

pygame.init()

rock = pygame.image.load('rock.png')

X = 500
Y = 500
win = pygame.display.set_mode((X, Y))

pygame.display.set_caption("My Game")
score = 0


class player(object):
    def __init__(self, x, y, width, height, vel):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel
        self.rect = pygame.Rect((self.x, self.y), (self.width, self.height))

    def draw(self):
        # win.blit(pygame.draw.rect(win, (255, 0, 0), (self.x, self.y, self.width, self.height)))
        pygame.draw.rect(win, (255, 0, 0), (self.x, self.y, self.width, self.height))




class enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, vel):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel
        self.rect = pygame.Rect((self.x, self.y), (self.width, self.height))

    def draw(self):
        # win.blit(rock, (self.x, self.y))
        pygame.draw.rect(win, (0, 0, 255), (self.x, self.y, self.width, self.height))

    def is_collided_with(self, player):
        collide = False
        if player.x <= self.x <= player.x + player.width and player.y <= self.y <= player.y + player.height:
            collide = True
        if player.x <= self.x + self.width <= player.x + player.width and player.y <= self.y <= player.y + player.height:
            collide = True
        if player.x <= self.x <= player.x + player.width and self.y + self.height >= player.y and self.y + self.height <= player.y + player.height:
            collide = True
        if player.x <= self.x + self.width <= player.x + player.width and self.y + self.height >= player.y and self.y + self.height <= player.y + player.height:
            collide = True
        return collide

    # def kill(self):
    #     self.kill()


player = player((X - 50) // 2, 440, 50, 10, 10)
enemy = enemy((X - 10) // 2, 50, 10, 10, 5)


def redrawGameWindow():
    win.fill((0, 0, 0))  # Fills the screen with black

    font = pygame.font.SysFont("comicsans", 20, True)
    text = font.render('Your score: ' + str(score), 1, (255, 0, 0))
    win.blit(text, (0, 10))

    # win.blit(bg, (0, 0))
    player.draw()
    enemy.draw()
    # print(player.is_collided_with(enemy))
    pygame.display.update()
    if enemy.y == Y:
        enemy.y = 0
        enemy.x = np.random.randint(0, X-enemy.width)


run = True
gameover = False

while run:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    enemy.y += enemy.vel

    if keys[pygame.K_LEFT]:
        player.x -= player.vel

    if keys[pygame.K_RIGHT]:
        player.x += player.vel


    if enemy.is_collided_with(player):
        font = pygame.font.SysFont("comicsans", 30, True)
        text = font.render('You are hit', 1, (255, 0, 0))
        win.blit(text, (390, 10))
        score += 1
        enemy.y = 0
        enemy.x = np.random.randint(0, X - enemy.width)
        # enemy.kill()


    redrawGameWindow()

pygame.quit()
