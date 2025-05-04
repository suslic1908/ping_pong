import pygame
import sys

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("ping-pong")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

player_image = pygame.image.load('cube yelou.jpg')
scaled_player_image = pygame.transform.scale(player_image, (30, 150 ))
keys = pygame.key.get_pressed()

class Player():
    def __init__(self, x, key_up, key_down):
        self.x = x
        self.y = 200
        self.key_up = key_up
        self.key_down = key_down

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[self.key_up]:
            self.y -= 0.5
        if keys[self.key_down]:
            self.y += 0.5

    def draw(self, surface):
        surface.blit(scaled_player_image, (self.x, self.y))

class ball():
    def __init__(self, x, y):
        self.x = x
        self.y =y

player1 = Player(0, pygame.K_w, pygame.K_s)
player2 = Player(770, pygame.K_UP, pygame.K_DOWN)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player1.move()
    player2.move()

    screen.fill((255, 255, 255))

    player1.draw(screen)
    player2.draw(screen)

    pygame.display.flip()

pygame.quit()




