import pygame, sys
from pygame.locals import *

#Start de pygame
pygame.init()

#Ventana
PANTALLA = pygame.display.set_mode((1280,720))
pygame.display.set_caption("Proyecto")

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
    pygame.display.update()
    eso tilin
