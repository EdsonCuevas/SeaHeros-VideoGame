import pygame, sys
from pygame.locals import *
import random

def nivel1():

    #Start de pygame
    pygame.init()

#Pantalla
W,H = 720,720
PANTALLA = pygame.display.set_mode((W,H))
pygame.display.set_caption("Sea Heroes")

#Fondo
fondo = pygame.image.load("img/ocean.jpg").convert()
VelFondo = 0

#Variables Principales
FPS = 100
Reloj = pygame.time.Clock()
nadando = False
game_over = False

frecuencia_botella = 1500 #milisegundos
ultima_botella = pygame.time.get_ticks() - frecuencia_botella

frecuencia_bag = 2000 #milisegundos
ultima_bag = pygame.time.get_ticks() - frecuencia_bag

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
        if nadando == True:
            self.vel += 0.5
            if self.vel > 8:
                self.vel = 8
            if self.rect.bottom < 720:
                self.rect.y += int(self.vel)

        if game_over == False:
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
        else:
            self.image = pygame.transform.rotate(self.images[self.index], -180)

#La clase de la botella
class Bottle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/botella.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = [x,y]

    def update(self):
        #Se quedan en su lugar al morir
        if game_over == False:
            self.rect.x -= 2
            
        if self.rect.right < 0:
            self.kill()

#La clase de la bolsa
class Bag(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/bolsa.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = [x,y]

    def update(self):
        #Se quedan en su lugar al morir
        if game_over == False:
            self.rect.x -= 2
            
        if self.rect.right < 0:
            self.kill()

#Se declaran los objetos como grupos
fish_group = pygame.sprite.Group()
bottle_group = pygame.sprite.Group()
bag_group = pygame.sprite.Group()

#Cordenadas donde aparece el pescado
flappy = Fish(100, int(W / 1.6))
fish_group.add(flappy)

#Bucle para que no se cierre el juego
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and nadando == False and game_over == False:
            nadando = True

    #Movimiento en bucle del fondo del juego
    x_relativa = VelFondo % fondo.get_rect().width
    PANTALLA.blit(fondo,(x_relativa - fondo.get_rect().width,0))
    if x_relativa < W:
        PANTALLA.blit(fondo,(x_relativa,0))
    #Velocidad del fondo
    VelFondo -= 2
    Reloj.tick(FPS)

    #Muestra todo en pantalla
    fish_group.draw(PANTALLA)
    fish_group.update()
    bottle_group.draw(PANTALLA)
    bottle_group.update()
    bag_group.draw(PANTALLA)
    bag_group.update()

    #Revisa que el pescado no se salga del agua
    if flappy.rect.top < 200:
        flappy.rect.top = 200
    
    #Revisa la colision
    if pygame.sprite.groupcollide(fish_group, bottle_group, False, False):
        game_over = True
    if pygame.sprite.groupcollide(fish_group, bag_group, False, False):
        game_over = True
        
    #Revisa que el pescado toque el suelo
    if flappy.rect.bottom >= 720:
        game_over = True
        nadando = False
    if game_over == True:
        VelFondo = 0


    if game_over == False and nadando == True:
        #Generador de botella
        time_now = pygame.time.get_ticks()
        if time_now - ultima_botella > frecuencia_botella:
            bottle_spawn = random.randint(-100, 200)
            bottle = Bottle(W, int(H / 2) + bottle_spawn)
            bottle_group.add(bottle)
            ultima_botella = time_now

    if game_over == False and nadando == True:
        #Generador de bolsa
        time_now = pygame.time.get_ticks()
        if time_now - ultima_bag > frecuencia_bag:
            bag_spawn = random.randint(-100, 200)
            bag = Bag(W, int(H / 2) + bag_spawn)
            bag_group.add(bag)
            ultima_bag = time_now

    pygame.display.update()