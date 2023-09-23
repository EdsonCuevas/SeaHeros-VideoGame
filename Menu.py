import pygame, sys
from button import Button
from pygame.locals import *

pygame.init()

W, H = 1280, 720
SCREEN = pygame.display.set_mode((W, H), pygame.RESIZABLE)
pygame.display.set_caption("Sea Heros")

BG = pygame.image.load("assets/Background.png")

music = pygame.mixer.Sound("ost/menu.mp3")


def get_font(size):
        return pygame.font.Font("assets/font.ttf", size)

def play():
        while True:

            
            #Carga la posicion del mouse
            PLAY_MOUSE_POS = pygame.mouse.get_pos()

            #Carga de fondo para nuevas ventanas
            SCREEN.fill("black")
            SCREEN.blit(BG, (0, 0))

            #Carga un titulo con sus fuentes y tamaños
            PLAY_TEXT = get_font(45).render("Selecciona la dificultad", True, "White")
            PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 90))
            SCREEN.blit(PLAY_TEXT, PLAY_RECT)

            #Carga el boton de inicio de nivel facil
            EASY_GAME = Button(image=(None), pos=(640, 300),
                                text_input="EASY", font=get_font(75), base_color="White", hovering_color="Green")
            
            #Carga el boton de inicio de nivel dificil
            HARD_GAME = Button(image=(None), pos=(640, 400),
                                text_input="HARD", font=get_font(75), base_color="White", hovering_color="Green")

            #Carga un boton de volver al menu
            PLAY_BACK = Button(image=None, pos=(640, 600), 
                                text_input="VOLVER", font=get_font(75), base_color="White", hovering_color="Green")

            #Muestra los botones y pantalla actualizados
            PLAY_BACK.changeColor(PLAY_MOUSE_POS)
            PLAY_BACK.update(SCREEN)
            EASY_GAME.changeColor(PLAY_MOUSE_POS)
            EASY_GAME.update(SCREEN)
            HARD_GAME.changeColor(PLAY_MOUSE_POS)
            HARD_GAME.update(SCREEN)

            #Bucle para cerrar el juego
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                #Ejecucion del boton de volver
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                        main_menu()
                #Ejecucion del boton de nivel facil
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if EASY_GAME.checkForInput(PLAY_MOUSE_POS):
                        from Game import nivelfacil
                        nivelfacil()

            pygame.display.update()
            
        
def options():
        while True:
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

            SCREEN.fill("white")

            OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
            OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
            SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

            OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                                text_input="VOLVER", font=get_font(75), base_color="Black", hovering_color="Green")

            OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
            OPTIONS_BACK.update(SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                        main_menu()

            pygame.display.update()

def main_menu():
    while True:
            SCREEN.blit(BG, (0, 0))

            MENU_MOUSE_POS = pygame.mouse.get_pos()

            MENU_TEXT = get_font(100).render("SEA HEROS", True, "#b68f40")
            MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

            PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250), 
                                text_input="JUGAR", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
            OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400), 
                                text_input="OPCIONES", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
            QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550), 
                                text_input="SALIR", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

            SCREEN.blit(MENU_TEXT, MENU_RECT)

            for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(SCREEN)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        play()
                    if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                        options()
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        sys.exit()
                

            pygame.display.update()

main_menu()