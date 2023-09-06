import pygame, sys
from pygame.locals import *

#Start de pygame
pygame.init()   

#Pantalla
W,H = 720,625
PANTALLA = pygame.display.set_mode((W,H))
pygame.display.set_caption("Sea Heroes")
FPS = 100
Reloj = pygame.time.Clock()

#Fondo
fondo=pygame.image.load("img/ocean.jpg").convert()
x=0

class Fish(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/fish.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

fish_group = pygame.sprite.Group()

flappy = Fish(100, int(W / 1.7))

fish_group.add(flappy)

#Bucle para que no se cierre el juego
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    x_relativa = x % fondo.get_rect().width
    PANTALLA.blit(fondo,(x_relativa - fondo.get_rect().width,0))
    if x_relativa < W:
        PANTALLA.blit(fondo,(x_relativa,0))

    x -= 1
    Reloj.tick(FPS)
    fish_group.draw(PANTALLA)
    pygame.display.update()