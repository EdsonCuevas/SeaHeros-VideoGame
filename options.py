import pygame, sys
from pygame.locals import *

def opciones():
    
        #Inicializacion de la ventana
        pygame.init()

        w,h = 1280, 720
        SCREEN = pygame.display.set_mode((w,h))
        pygame.display.set_caption("Controles")

        BG = pygame.image.load("assets/background_control.png").convert()

        #funcion principal de los controles
        def menu_opcion():
            while True:  
                #Exit de esta ventana
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    pygame.mouse.get_pos()

                SCREEN.blit(BG, (0, 0))
                pygame.display.update()

        menu_opcion()              

        
                
      
             

opciones()