import pygame, sys
from pygame.locals import *

#Start de pygame
pygame.init()   

#Pantalla
W,H = 720,630
PANTALLA = pygame.display.set_mode((W,H))
pygame.display.set_caption("Sea Heroes")
FPS = 100
Reloj = pygame.time.Clock()

#Fondo
fondo=pygame.image.load("img/ocean.jpg").convert()
x=0

#Todas las funciones del pescado
class Fish(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/fish1.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.vel = 0
        self.clicked = False

    def update(self):

        #Gravedad del pescado
        self.vel += 0.5
        if self.vel > 8:
            self.vel = 8
        if self.rect.bottom < 630:
            self.rect.y += int(self.vel)

        #Salto del pescado
        if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
            self.clicked = True
            self.vel = -10
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        #Rotacion
        #self.image = pygame.transform.rotate()


fish_group = pygame.sprite.Group()

flappy = Fish(100, int(W / 2))

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
    fish_group.update()
    pygame.display.update()