import pygame, sys
from pygame.locals import *

#Start de pygame
pygame.init()

#Pantalla
W,H = 450,450
PANTALLA = pygame.display.set_mode((W,H))
pygame.display.set_caption("Sea Heroes")
FPS = 100
Reloj = pygame.time.Clock()

#Fondo
fondo=pygame.image.load("oceano.jpg").convert()
x=0

#Colores
Blanco = (255,255,255)
Negro = (0,0,0)
Rojo = (255,0,0)
Azul = (0,0,255)
Verde = (0,255,0)

PANTALLA.fill(Blanco)

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
    pygame.display.update()
    Reloj.tick(FPS)