import pygame, sys
from pyvidplayer import Video
from button import Button
from pygame.locals import *
from JSON import Load

#Carga el .JSON
Configuracion, langueje = Load()

#Inicia el juego pygame
pygame.init()

#Declaro las variables para el ancho y alto del juego
#Resolucion
W, H = 1280, 720
PANTALLA = pygame.display.set_mode((W, H))
pygame.display.set_caption("Sea Heros")

muted = False
Music = pygame.mixer_music.get_volume()

#Meto la imagenes del click en una variable
click1 = pygame.image.load("img/keys/mouse_L_pressed_paper.png")

#Declaro las imagenes de todas las funciones de sonido
sonido_arriba = pygame.image.load("sound/img/volume_up.png")
sonido_abajo = pygame.image.load("sound/img/volume_down.png")
sonido_mute = pygame.image.load("sound/img/volume_muted.png")
sonido_max = pygame.image.load("sound/img/volume_max.png")

#Declaro las fuentes
font2 = pygame.font.Font('assets/upheavtt.ttf', 40)
font3 = pygame.font.Font('assets/upheavtt.ttf', 22)

#Declaro colores que usare en las fuentes
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 208, 0)
red = (255, 0, 0)

#Reloj
reloj = pygame.time.get_ticks()

#Cargo el video de intro y su resolucion
vid = Video("videoxd.mp4")
vid.set_size((1280, 720))

#Funcion con sus atributos para generar texto en la pantalla 
def draw_text(text, font, text_col, x,y):
            img = font.render(text, True, text_col)
            PANTALLA.blit(img, (x,y))

def intro():
    run = True
    while run:
        #Carga el video de la intro
        vid.draw(PANTALLA, (0,0))
        if langueje == "en":
            draw_text(Configuracion.get(langueje, {}).get("skipintro"), font2, black, 900, 670)
            PANTALLA.blit(click1, (1015, 645))
        if langueje == "es":
            draw_text(Configuracion.get(langueje, {}).get("skipintro"), font2, black, 760, 670)
            PANTALLA.blit(click1, (945, 645))

        #Si el juego ya esta iniciado no vuelve a cargar la intro de nuevo
        if reloj >= 1000:
            vid.close()
            run = False
            MenuTotal()
        
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                vid.close()
                run = False
                MenuTotal()
            
def MenuTotal():

    #Cargo el .JSON
    Configuracion, langueje = Load()

    #Inicia el juego pygame
    pygame.init()

    #Resolucion declarada en variables
    W, H = 1280, 720
    #Se declara PANTALLA que sera el display del juego
    PANTALLA = pygame.display.set_mode((W, H))
    #Nombre de la ventana
    pygame.display.set_caption("Sea Heros")

    #Carga el fondo del menu principal
    BG = pygame.image.load("assets/Background.png")

    #Carga la musica
    pygame.mixer.music.load("sound/menu.mp3")

    #Carga el volumen inicial
    pygame.mixer.music.set_volume(0.5)

    #Carga la musica en bucle con el -1
    pygame.mixer.music.play(-1)

    #Carga las imagenes la funcion de volumen en una variable
    sonido_arriba = pygame.image.load("sound/img/volume_up.png")
    sonido_abajo = pygame.image.load("sound/img/volume_down.png")
    sonido_mute = pygame.image.load("sound/img/volume_muted.png")
    sonido_max = pygame.image.load("sound/img/volume_max.png")

    #La funcion de el control de volumen
    def ControlMusic():
        #Control del audio
                #Baja volumen si se mantiene presionada
                keys = pygame.key.get_pressed()
                if keys[pygame.K_DOWN] and pygame.mixer_music.get_volume() > 0.0:
                    pygame.mixer.music.set_volume(pygame.mixer_music.get_volume() - 0.01)
                    PANTALLA.blit(sonido_abajo, (1150,25))
                elif keys[pygame.K_DOWN] and pygame.mixer_music.get_volume() == 0.0:
                    PANTALLA.blit(sonido_mute, (1150,25))

                #Sube volumen si se mantiene presionada
                if keys[pygame.K_UP] and pygame.mixer_music.get_volume() < 1.0:
                    pygame.mixer.music.set_volume(pygame.mixer_music.get_volume() + 0.01)
                    PANTALLA.blit(sonido_arriba, (1150,25))
                elif keys[pygame.K_UP] and pygame.mixer_music.get_volume() == 1.0:
                    PANTALLA.blit(sonido_max, (1150,25))


    #Carga una fuente para el Titulo del juego
    def get_font(size):
            return pygame.font.Font("assets/font.ttf", size)

    #El menu de play
    def play():
            while True:

                #Carga la posicion del mouse
                PLAY_MOUSE_POS = pygame.mouse.get_pos()

                #Carga de fondo para nuevas ventanas
                PANTALLA.fill("black")
                PANTALLA.blit(BG, (0, 0))

                #Carga un titulo con sus fuentes y tamaños
                PLAY_TEXT = get_font(45).render(Configuracion.get(langueje, {}).get("select"), True, "White")
                PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 50))
                PANTALLA.blit(PLAY_TEXT, PLAY_RECT)

                #Carga el boton de inicio de nivel facil
                EASY_GAME = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 260),
                                    text_input=Configuracion.get(langueje, {}).get("easy"), font=get_font(75), base_color="White", hovering_color="Green")
                
                #Carga el boton de inicio de nivel dificil
                if (langueje == "en"):
                    HARD_GAME = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 400),
                                        text_input=Configuracion.get(langueje, {}).get("hard"), font=get_font(75), base_color="White", hovering_color="Green")
                if (langueje == "es"):
                    HARD_GAME = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400),
                                        text_input=Configuracion.get(langueje, {}).get("hard"), font=get_font(75), base_color="White", hovering_color="Green")

                #Carga un boton de volver al menu
                PLAY_BACK = Button(image=None, pos=(640, 600), 
                                    text_input=Configuracion.get(langueje, {}).get("back"), font=get_font(75), base_color="White", hovering_color="Red")

                #Muestra los botones y PANTALLA actualizados
                PLAY_BACK.changeColor(PLAY_MOUSE_POS)
                PLAY_BACK.update(PANTALLA)
                EASY_GAME.changeColor(PLAY_MOUSE_POS)
                EASY_GAME.update(PANTALLA)
                HARD_GAME.changeColor(PLAY_MOUSE_POS)
                HARD_GAME.update(PANTALLA)

                #Bucle para cerrar el juego
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    #Ejecucion del boton de volver
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                            main_menu()
                    #Ejecucion del boton del modo facil
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if EASY_GAME.checkForInput(PLAY_MOUSE_POS):
                            pygame.mixer_music.stop()
                            from GameEasy import start_menu
                            start_menu()
                    #Ejecucion del boton del modo dificil
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if HARD_GAME.checkForInput(PLAY_MOUSE_POS):
                            pygame.mixer_music.stop()
                            from GameHard import Level1
                            Level1()
                            
                ControlMusic()
                pygame.display.update()

    #El menu de opciones            
    def options():
            while True:
                OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

                PANTALLA.blit(BG, (0, 0))

                #Detector de mute
                if pygame.mixer_music.get_volume() == 0.0:
                    muted = True
                    infoaud = Configuracion.get(langueje, {}).get("muted")
                if pygame.mixer_music.get_volume() >= 0.1:
                    muted = False                
                    infoaud = Configuracion.get(langueje, {}).get("unmuted")

                #Muestra Texto Titulo Opciones
                OPTIONS_TEXT = get_font(45).render(Configuracion.get(langueje, {}).get("option"), True, "White")
                OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 90))
                PANTALLA.blit(OPTIONS_TEXT, OPTIONS_RECT)

                #Muestra Texto de Idioma
                IDIOMA_TEXT = get_font(45).render(Configuracion.get(langueje, {}).get("language"), True, "White")
                IDIOMA_RECT = IDIOMA_TEXT.get_rect(center=(500, 250))
                PANTALLA.blit(IDIOMA_TEXT, IDIOMA_RECT)

                #Muestra Texto de Volumen
                MUSICVOL_TEXT = get_font(45).render(Configuracion.get(langueje, {}).get("musictext"), True, "White")
                MUSICVOL_RECT = IDIOMA_TEXT.get_rect(center=(500, 400))
                PANTALLA.blit(MUSICVOL_TEXT, MUSICVOL_RECT)

                #Boton de cambio de idioma
                CHANGE_LANG = Button(image=(pygame.image.load("assets/Play Rect.png")), pos=(900, 250),
                                    text_input=Configuracion.get(langueje, {}).get("changelanguage"), font=get_font(50), base_color="White", hovering_color="Green")
                
                #Boton de Desactivador de Musica
                if(langueje == "es"):
                    MUSIC = Button(image=(pygame.image.load("assets/Play Rect.png")), pos=(850, 400),
                                        text_input=infoaud, font=get_font(50), base_color="White", hovering_color="Green")
                
                if(langueje == "en"):
                    MUSIC = Button(image=(pygame.image.load("assets/Play Rect.png")), pos=(750, 400),
                                        text_input=infoaud, font=get_font(50), base_color="White", hovering_color="Green")
                    
                FULLSCREEN = Button(image=None, pos=(650, 520),
                                    text_input=Configuracion.get(langueje, {}).get("fullscreen"), font=get_font(50), base_color="White", hovering_color="Green")
                

                #Boton de Salir
                OPTIONS_BACK = Button(image=None, pos=(640, 650), 
                                    text_input="VOLVER", font=get_font(75), base_color="White", hovering_color="Red")
                
                #Bucle para indicar cuando se cierra la ventana
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    #Detecta si la tecla del mouse es presionada
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                            main_menu()

                        if CHANGE_LANG.checkForInput(OPTIONS_MOUSE_POS):
                            pass

                        if muted == False:
                            if MUSIC.checkForInput(OPTIONS_MOUSE_POS):
                                pygame.mixer_music.set_volume(0.0)
                                
                        if muted == True:
                            if MUSIC.checkForInput(OPTIONS_MOUSE_POS):
                                pygame.mixer_music.set_volume(0.5)
                                
                                

                OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
                OPTIONS_BACK.update(PANTALLA)
                CHANGE_LANG.changeColor(OPTIONS_MOUSE_POS)
                CHANGE_LANG.update(PANTALLA)
                MUSIC.changeColor(OPTIONS_MOUSE_POS)
                MUSIC.update(PANTALLA)
                FULLSCREEN.changeColor(OPTIONS_MOUSE_POS)
                FULLSCREEN.update(PANTALLA)

                
                                 

                ControlMusic()

                pygame.display.update()

    def main_menu():
        while True:
                #Ejectua el fondo previamente cargado en la variable BG
                PANTALLA.blit(BG, (0, 0))
                
                #Detecta la posicion del mouse para poder interactuar con los botones
                MENU_MOUSE_POS = pygame.mouse.get_pos()

                MENU_TEXT = get_font(100).render("SEA HEROS", True, "#b68f40")
                MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))


                PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250), 
                                    text_input=Configuracion.get(langueje, {}).get("play"), font=get_font(75), base_color="Green", hovering_color="White")
                OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400), 
                                    text_input=Configuracion.get(langueje, {}).get("option"), font=get_font(75), base_color="Blue", hovering_color="White")
                QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550), 
                                    text_input=Configuracion.get(langueje, {}).get("exit"), font=get_font(75), base_color="Red", hovering_color="White")

                PANTALLA.blit(MENU_TEXT, MENU_RECT)

                for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
                    button.changeColor(MENU_MOUSE_POS)
                    button.update(PANTALLA)
                
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
    
intro()