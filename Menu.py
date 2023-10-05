import pygame, sys
from button import Button
from pygame.locals import *
from JSON import Load


def MenuTotal():

    Configuracion, langueje = Load()

    pygame.init()

    W, H = 1280, 720
    SCREEN = pygame.display.set_mode((W, H), pygame.RESIZABLE)
    pygame.display.set_caption("Sea Heros")

    BG = pygame.image.load("assets/background_control.png")

    #Music
    pygame.mixer.music.load("sound/menu.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
    sonido_arriba = pygame.image.load("sound/img/volume_up.png")
    sonido_abajo = pygame.image.load("sound/img/volume_down.png")
    sonido_mute = pygame.image.load("sound/img/volume_muted.png")
    sonido_max = pygame.image.load("sound/img/volume_max.png")


    def ControlMusic():
        #Control del audio
                #Baja volumen
                keys = pygame.key.get_pressed()
                if keys[pygame.K_DOWN] and pygame.mixer_music.get_volume() > 0.0:
                    pygame.mixer.music.set_volume(pygame.mixer_music.get_volume() - 0.01)
                    SCREEN.blit(sonido_abajo, (1150,25))
                elif keys[pygame.K_DOWN] and pygame.mixer_music.get_volume() == 0.0:
                    SCREEN.blit(sonido_mute, (1150,25))

                #Sube volumen
                if keys[pygame.K_UP] and pygame.mixer_music.get_volume() < 1.0:
                    pygame.mixer.music.set_volume(pygame.mixer_music.get_volume() + 0.01)
                    SCREEN.blit(sonido_arriba, (1150,25))
                elif keys[pygame.K_UP] and pygame.mixer_music.get_volume() == 1.0:
                    SCREEN.blit(sonido_max, (1150,25))

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
                PLAY_TEXT = get_font(45).render(Configuracion.get(langueje, {}).get("select"), True, "White")
                PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 100))
                SCREEN.blit(PLAY_TEXT, PLAY_RECT)

                #Carga el boton de inicio de nivel facil
                EASY_GAME = Button(image=(None), pos=(640, 300),
                                    text_input=Configuracion.get(langueje, {}).get("easy"), font=get_font(75), base_color="White", hovering_color="Green")
                
                #Carga el boton de inicio de nivel dificil
                HARD_GAME = Button(image=(None), pos=(640, 400),
                                    text_input=Configuracion.get(langueje, {}).get("hard"), font=get_font(75), base_color="White", hovering_color="Green")

                #Carga un boton de volver al menu
                PLAY_BACK = Button(image=None, pos=(640, 600), 
                                    text_input=Configuracion.get(langueje, {}).get("back"), font=get_font(75), base_color="White", hovering_color="Red")

                #Muestra los botones y SCREEN actualizados
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
                            from Game import nivelfacil1
                            nivelfacil1()
                            
                ControlMusic()
                pygame.display.update()
                
    def options():
            while True:
                OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

                SCREEN.blit(BG, (0, 0))

                OPTIONS_TEXT = get_font(45).render("Esta es el menu de controles", True, "Black")
                OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
                SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

                OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                                    text_input="VOLVER", font=get_font(75), base_color="Black", hovering_color="Red")

                OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
                OPTIONS_BACK.update(SCREEN)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                            main_menu()

                ControlMusic()

                pygame.display.update()

    def main_menu():
        while True:
                SCREEN.blit(BG, (0, 0))
                

                MENU_MOUSE_POS = pygame.mouse.get_pos()

                MENU_TEXT = get_font(100).render("SEA HEROS", True, "#b68f40")
                MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

                PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250), 
                                    text_input=Configuracion.get(langueje, {}).get("play"), font=get_font(75), base_color="#d7fcd4", hovering_color="White")
                OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400), 
                                    text_input=Configuracion.get(langueje, {}).get("option"), font=get_font(75), base_color="#d7fcd4", hovering_color="White")
                QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550), 
                                    text_input=Configuracion.get(langueje, {}).get("exit"), font=get_font(75), base_color="#d7fcd4", hovering_color="White")

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

                ControlMusic()
                pygame.display.update()

    main_menu()
MenuTotal()
