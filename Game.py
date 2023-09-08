import pygame, sys
from pygame.locals import *

#Start de pygame
pygame.init()   

#Pantalla
W,H = 720,630
PANTALLA = pygame.display.set_mode((W,H))
pygame.display.set_caption("Sea Heroes")

#Fondo
fondo=pygame.image.load("img/ocean.jpg").convert()
x=0

#Variables Principales
FPS = 100
Reloj = pygame.time.Clock()
flying = False
game_over = False

#Todas las funciones del pescado
class Fish(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        for num in range (1, 4):
            img = pygame.image.load(f"img/Fish animation/fish{num}.png")
            self.images.append(img)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.vel = 0
        self.clicked = False

    def update(self):

        #Gravedad del pescado
        if flying == True:
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

        #Animaciones del pescado
        self.counter += 1
        flap_cooldown = 10

        if self.counter > flap_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
        self.image = self.images[self.index]

        #Rotacion del pescado
        self.image = pygame.transform.rotate(self.images[self.index], self.vel * -1)


fish_group = pygame.sprite.Group()
#El lugar donde empieza el Pescado
flappy = Fish(100, int(W / 2))

fish_group.add(flappy)

#Bucle para que no se cierre el juego
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and flying == False and game_over == False:
            flying = True

    #Movimiento en bucle del fondo del juego
    x_relativa = x % fondo.get_rect().width
    PANTALLA.blit(fondo,(x_relativa - fondo.get_rect().width,0))
    if x_relativa < W:
        PANTALLA.blit(fondo,(x_relativa,0))
    #Velocidad del fondo
    x -= 2
    Reloj.tick(FPS)

    fish_group.draw(PANTALLA)
    fish_group.update()

    #Revisa que el pescado toque el suelo
    if flappy.rect.bottom > 629:
        game_over = True
        flying = False

    if game_over == True:
        x = 0

    pygame.display.update()