import pygame, sys, time
from pyvidplayer import Video
from button import Button
from pygame.locals import *
from JSON  import Load

#Inicia el juego pygame
pygame.init()

#Cargo el JSON
Configuracion, langueje = Load()

#Declaro las variables para el ancho y alto del juego
#Resolucion
W, H = 1280, 720
#Setea el display en una variable
PANTALLA = pygame.display.set_mode((W, H))
#Nombre de la ventana del juego
pygame.display.set_caption("Sea Hereos")

#Crea un variable booleana
muted = False

#En music guarda el porcentaje de volumen actual de 0.1 - 1.0
Music = pygame.mixer_music.get_volume()

#Declara el idioma actual en español
idioma_actual = "es"

#Meto la imagenes del click en una variable para usarlo en el intro
click1 = pygame.image.load("img/Sprites/Keys/mouse_L_pressed_paper.png")

#Carga las imagenes de control de volumen
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

#En una variable guardo el tiempo en milisegundos que transcurren desde que se inicia el pygame.init
reloj = pygame.time.get_ticks()

#Cargo el video de intro
vid = Video("assets/intro.mp4")
#Setea la resolucion del video en HD
vid.set_size((1280, 720))

#Funcion con sus atributos para generar texto en la pantalla 
def draw_text(text, font, text_col, x,y):
            img = font.render(text, True, text_col)
            PANTALLA.blit(img, (x,y))

#Funcion para la intro al abrir el juego
def intro():
    
    #Bucle while para cargar el video y texto
    run = True
    while run:

        #Carga el video de la intro
        vid.draw(PANTALLA, (0,0))
        if langueje == "en":
            draw_text(Configuracion.get(langueje, {}).get("skipintro"), font2, white, 20, 670)
            PANTALLA.blit(click1, (134, 645))
        if langueje == "es":
            draw_text(Configuracion.get(langueje, {}).get("skipintro"), font2, white, 20, 670)
            PANTALLA.blit(click1, (205, 645))

        #Si el juego ya esta iniciado no vuelve a cargar la intro de nuevo
        if reloj >= 1000:
            vid.close()
            run = False
            MenuTotal()

        #Bucle for para que la ventana del juego se pueda cerrar
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #Detecta si el mouse se presiona
            if event.type == pygame.MOUSEBUTTONDOWN:
                #Cierra el video
                vid.close()
                #Termina el bucle
                run = False
                #Carga la funcion del Menu
                MenuTotal()

        #Funcion predefinida para la actualizacion de pantalla
        pygame.display.update()
            
def MenuTotal():

    #La declaro la variable languaje como global para que se pueda ver el cambio de idioma en esta parte del Menu
    global langueje
    #Carga el JSON
    Configuracion, langueje = Load()
    
    #Inicia el juego pygame
    pygame.init()

    #Resolucion declarada en variables
    W, H = 1280, 720
    #Se declara PANTALLA que sera el display del juego
    PANTALLA = pygame.display.set_mode((W, H))
    #Nombre de la ventana
    pygame.display.set_caption("Sea Heroes")

    #Carga el fondo del menu principal en una variable
    BG = pygame.image.load("img/Backgrounds/Background_menu.png")

    #Carga la musica
    pygame.mixer.music.load("sound/menu.mp3")

    #Setea el volumen inicial
    pygame.mixer.music.set_volume(0.5)

    #Carga la musica en bucle con el (-1)
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

                #La declaro la variable languaje como global para que se pueda ver el cambio de idioma en esta parte del Menu
                global langueje

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
                if langueje == "en": 
                    EASY_GAME = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 260),
                                        text_input=Configuracion.get(langueje, {}).get("easy"), font=get_font(75), base_color="White", hovering_color="Green")
                if langueje == "es": 
                    EASY_GAME = Button(image=pygame.image.load("assets/Play Rect1.png"), pos=(640, 260),
                                        text_input=Configuracion.get(langueje, {}).get("easy"), font=get_font(75), base_color="White", hovering_color="Green")
                
                #Carga el boton de inicio de nivel dificil
                if langueje == "en":
                    HARD_GAME = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 400),
                                        text_input=Configuracion.get(langueje, {}).get("hard"), font=get_font(75), base_color="White", hovering_color="Green")
                if langueje == "es":
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
                            return

                    #Ejecucion del boton del modo facil
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if EASY_GAME.checkForInput(PLAY_MOUSE_POS):
                            SelectorEasy()
                        
                    #Ejecucion del boton del modo dificil
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if HARD_GAME.checkForInput(PLAY_MOUSE_POS):
                            SelectorHard()
                            
                            
                ControlMusic()
                pygame.display.update()

    def SelectorEasy():

        #Carga de idioma
        global langueje
        

        #Funcion de texto
        def draw_text(text, font, text_col, x,y):
                    img = font.render(text, True, text_col)
                    PANTALLA.blit(img, (x,y))

        #Fuentes
        font2 = pygame.font.Font('assets/upheavtt.ttf', 50)
        font3 = pygame.font.Font('assets/upheavtt.ttf', 40)

        #Carga de imagenes
        bg = pygame.image.load("img/Backgrounds/Background_menu.png")
        level1 = pygame.image.load("img/Backgrounds/Background_level1.jpg")
        level2 = pygame.image.load("img/Backgrounds/Background_level2.png")
        level3= pygame.image.load("img/Backgrounds/Background_level2.png")
        submarine = pygame.image.load("img/Sprites/Submarine/submarine1.png")

        #Redimencionamiento de imagenes
        newLevel1 = pygame.transform.scale(level1,(250,250))
        newLevel2 = pygame.transform.scale(level2,(250,250))
        newLevel3 = pygame.transform.scale(level3,(250,250))
        newSubmarine = pygame.transform.scale(submarine,(150,100))

        #Convertir el fondo a objecto
        BacknewLevel1 = newLevel1.get_rect(topleft=(200, 200))  
        BacknewLevel2 = newLevel2.get_rect(topleft=(500, 200))  
        BacknewLevel3 = newLevel3.get_rect(topleft=(800, 200))

        #Funcion para la fuente del boton
        def get_font(size):
                return pygame.font.Font("assets/font.ttf", size)

        while True:    
            #Ventana
            PANTALLA.blit(bg,(0,0))

            #Mostrar fondos de cada nivel
            PANTALLA.blit(newLevel1, BacknewLevel1.topleft)
            PANTALLA.blit(newLevel2, BacknewLevel2.topleft)
            PANTALLA.blit(newLevel3, BacknewLevel3.topleft)
            

            #Mostrar texto en pantalla
            if langueje == "es":
                draw_text(Configuracion.get(langueje, {}).get("selectLevel"), font2, "white", 400,50)
            if langueje == "en":
                draw_text(Configuracion.get(langueje, {}).get("selectLevel"), font2, "white", 470,50)
            draw_text(Configuracion.get(langueje, {}).get("selectLevel1"), font3, "white", 250,470)
            draw_text(Configuracion.get(langueje, {}).get("selectLevel2"), font3, "white", 550,470)
            draw_text(Configuracion.get(langueje, {}).get("selectLevel3"), font3, "white", 850,470)

            #Obtener posicion del mouse
            PLAY_MOUSE_POS = pygame.mouse.get_pos()

            #(PENDIENTE)Animacion del personaje 
            if BacknewLevel1.collidepoint(PLAY_MOUSE_POS):
                #Crea una lista
                images = []
                #Forma para cambiar el numero al nombre de las imagenes
                for i in range(1,3):
                    name = "img/Sprites/Submarine/SubmarineRescale/submarine"+str(i)+".png"
                    images.append(pygame.image.load(name))
                #En una variable guarda la velocidad a la que cambia cada imagenes
                frame = int(time.time()*10) % 2
                #Muestra en pantalla cada imagen por frames
                PANTALLA.blit(images[frame], (275, 275))
                    
            if BacknewLevel2.collidepoint(PLAY_MOUSE_POS):
                    draw_text("hola", font2,"white",100,100)

            if BacknewLevel3.collidepoint(PLAY_MOUSE_POS):
                    draw_text("hola", font2,"white",100,100)

            #Salir
            BACK = Button(image=None, pos=(640, 600), 
                                        text_input=Configuracion.get(langueje, {}).get("back"), font=get_font(75), base_color="White", hovering_color="Red")
            
            BACK.changeColor(PLAY_MOUSE_POS)
            BACK.update(PANTALLA)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if BACK.checkForInput(PLAY_MOUSE_POS):
                        return

                #Entrar al nivel 1
                if event.type == pygame.MOUSEBUTTONDOWN:
                        if BacknewLevel1.collidepoint(PLAY_MOUSE_POS):
                            pygame.mixer_music.stop()
                            from GameEasy import load_level1
                            from GameEasy import Level1
                            load_level1()
                            Level1()
                
                #Entra al nivel 2
                if event.type == pygame.MOUSEBUTTONDOWN:
                        if BacknewLevel2.collidepoint(PLAY_MOUSE_POS):
                            pygame.mixer_music.stop()
                            from GameEasy import load_level2
                            from GameEasy import Level2
                            load_level2()
                            Level2()



            pygame.display.update()

    def SelectorHard():
        #Carga de idioma
        global langueje

        #Funcion de texto
        def draw_text(text, font, text_col, x,y):
                    img = font.render(text, True, text_col)
                    PANTALLA.blit(img, (x,y))

        #Parametros de la ventana
        w, h = 1280, 720
        PANTALLA = pygame.display.set_mode((w,h))

        #Fuentes
        font2 = pygame.font.Font('assets/upheavtt.ttf', 50)
        font3 = pygame.font.Font('assets/upheavtt.ttf', 40)

        #Carga de imagenes
        bg = pygame.image.load("img/Backgrounds/background_select.png")
        level1 = pygame.image.load("img/Backgrounds/Background_control.png")
        level2 = pygame.image.load("img/Backgrounds/Background_level2.png")
        level3= pygame.image.load("img/Backgrounds/Background_level3.jpg")
        fish = pygame.image.load("img/Sprites/FishAnimation/fish1.png")

        #Rendimencionamiento de imagenes
        newLevel1 = pygame.transform.scale(level1,(250,250))
        newLevel2 = pygame.transform.scale(level2,(250,250))
        newLevel3 = pygame.transform.scale(level3,(250,250))
        newFish = pygame.transform.scale(fish,(150,100))

        #Convertir el fondo a objecto
        BacknewLevel1 = newLevel1.get_rect(topleft=(200, 250))  
        BacknewLevel2 = newLevel2.get_rect(topleft=(500, 250))  
        BacknewLevel3 = newLevel3.get_rect(topleft=(800, 250)) 

        def get_font(size):
                return pygame.font.Font("assets/font.ttf", size)

        while True:    
            #Ventana
            PANTALLA.blit(bg,(0,0))

            #Mostrar fondos
            PANTALLA.blit(newLevel1, BacknewLevel1.topleft)
            PANTALLA.blit(newLevel2, BacknewLevel2.topleft)
            PANTALLA.blit(newLevel3, BacknewLevel3.topleft)
            PANTALLA.blit(newFish,(250,325))
            PANTALLA.blit(newFish,(550,325))
            PANTALLA.blit(newFish,(850,325))

            #Mostrar texto en pantalla
            if langueje == "es":
                draw_text(Configuracion.get(langueje, {}).get("selectLevel"), font2, "white", 400,50)
            if langueje == "en":
                draw_text(Configuracion.get(langueje, {}).get("selectLevel"), font2, "white", 470,50)
            draw_text(Configuracion.get(langueje, {}).get("selectLevel1"), font3, "white", 250,510)
            draw_text(Configuracion.get(langueje, {}).get("selectLevel2"), font3, "white", 550,510)
            draw_text(Configuracion.get(langueje, {}).get("selectLevel3"), font3, "white", 850,510)

            #Obtener posicion del mouse
            PLAY_MOUSE_POS = pygame.mouse.get_pos()

            #(PENDIENTE)Animacion del pez
            if BacknewLevel1.collidepoint(PLAY_MOUSE_POS):
                    draw_text("puta", font2,"white",100,100)
                    
            if BacknewLevel2.collidepoint(PLAY_MOUSE_POS):
                    draw_text("puta", font2,"white",100,100)

            if BacknewLevel3.collidepoint(PLAY_MOUSE_POS):
                    draw_text("puta", font2,"white",100,100)

            #Salir
            BACK = Button(image=None, pos=(640, 600), 
                                        text_input=Configuracion.get(langueje, {}).get("back"), font=get_font(75), base_color="White", hovering_color="Red")
            
            BACK.changeColor(PLAY_MOUSE_POS)
            BACK.update(PANTALLA)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if BACK.checkForInput(PLAY_MOUSE_POS):
                        return

                #(PENDIENTE)Entrar al nivel
                if event.type == pygame.MOUSEBUTTONDOWN:
                        if BacknewLevel1.collidepoint(PLAY_MOUSE_POS):
                            pygame.mixer_music.stop()
                            from GameHard import start_menu
                            from GameHard import Level1
                            start_menu()
                            Level1()



            pygame.display.update()

    #El menu de opciones            
    def options():
            while True:

                #La declaro la variable languaje como global para que se pueda ver el cambio de idioma en esta parte del Menu
                global langueje

                #La declaro la variable idioma_actual como global para poder almacenar el cambio de idioma
                global idioma_actual

                #Detecta la poicion del mouse y lo guarda en una varibale
                OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

                #Muestra en la pantalla el mismo background
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
                IDIOMA_TEXT = get_font(45).render(Configuracion.get(langueje, {}).get("language"), True, "Blue")
                IDIOMA_RECT = IDIOMA_TEXT.get_rect(center=(500, 250))
                PANTALLA.blit(IDIOMA_TEXT, IDIOMA_RECT)

                #Muestra Texto de Volumen
                MUSICVOL_TEXT = get_font(45).render(Configuracion.get(langueje, {}).get("musictext"), True, "Blue")
                MUSICVOL_RECT = IDIOMA_TEXT.get_rect(center=(500, 430))
                PANTALLA.blit(MUSICVOL_TEXT, MUSICVOL_RECT)

                #Boton de cambio de idioma
                if(langueje == "es"):
                    CHANGE_LANG_EN = Button(image=(pygame.image.load("assets/Play Rect.png")), pos=(850, 200),
                                        text_input=Configuracion.get(langueje, {}).get("changelanguage"), font=get_font(50), base_color="White", hovering_color="Green")
                    
                if(langueje == "en"):
                    CHANGE_LANG_EN = Button(image=(pygame.image.load("assets/Play Rect.png")), pos=(870, 200),
                                        text_input=Configuracion.get(langueje, {}).get("changelanguage"), font=get_font(50), base_color="Green", hovering_color="Green")
                
                if(langueje == "es"):
                    CHANGE_LANG_ES = Button(image=(pygame.image.load("assets/Play Rect.png")), pos=(850, 300),
                                        text_input=Configuracion.get(langueje, {}).get("changelanguage2"), font=get_font(50), base_color="Green", hovering_color="Green")
                    
                if(langueje == "en"):
                    CHANGE_LANG_ES = Button(image=(pygame.image.load("assets/Play Rect.png")), pos=(870, 300),
                                        text_input=Configuracion.get(langueje, {}).get("changelanguage2"), font=get_font(50), base_color="White", hovering_color="Green")
                
                #Boton de Desactivador de Musica
                if(langueje == "es"):
                    MUSIC = Button(image=(pygame.image.load("assets/Play Rect1.png")), pos=(850, 420),
                                        text_input=infoaud, font=get_font(50), base_color="White", hovering_color="Green")
                
                if(langueje == "en"):
                    MUSIC = Button(image=(pygame.image.load("assets/Play Rect.png")), pos=(750, 420),
                                        text_input=infoaud, font=get_font(50), base_color="White", hovering_color="Green")
                    
                
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
                        #Si el boton es presionado
                        if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                            #Retorna al main menu
                            return

                        #Si el boton de cambio de idioma ingles es presionado
                        if CHANGE_LANG_EN.checkForInput(OPTIONS_MOUSE_POS):
                            #Cambia las variables a en
                            langueje = "en"
                            idioma_actual = "en"
                        #Si el boton de cambio de idioma ingles es presionado
                        if CHANGE_LANG_ES.checkForInput(OPTIONS_MOUSE_POS):
                            #cambia las variables a en
                            langueje = "es"
                            idioma_actual = "es"

                            
                        #Si el juego no esta sin volumen
                        if muted == False:
                            #Si se da click en el boton de apagar
                            if MUSIC.checkForInput(OPTIONS_MOUSE_POS):
                                #Setea el volumen a 0
                                pygame.mixer_music.set_volume(0.0)
                        
                        #Si el juego ya esta muteado
                        if muted == True:
                            #Si el boton de cambio de mute es presionado
                            if MUSIC.checkForInput(OPTIONS_MOUSE_POS):
                                #Sube el volumen a la mitad
                                pygame.mixer_music.set_volume(0.5)
                                
                                
                #El cambio de color cuando el mouse esta encima del boton
                #Muestra contantemente los botones en la pantalla
                OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
                OPTIONS_BACK.update(PANTALLA)
                CHANGE_LANG_EN.changeColor(OPTIONS_MOUSE_POS)
                CHANGE_LANG_EN.update(PANTALLA)
                CHANGE_LANG_ES.changeColor(OPTIONS_MOUSE_POS)
                CHANGE_LANG_ES.update(PANTALLA)
                MUSIC.changeColor(OPTIONS_MOUSE_POS)
                MUSIC.update(PANTALLA)

                
                #Llamamos a la funcion de control de musica para que tambien funcione en este menu de opciones
                ControlMusic()

                #Para que el display este en contante actualizacion
                pygame.display.update()

    #Deffino la funcion del Menu principal
    def main_menu():
        while True:
                
                #La declaro la variable languaje como global para que se pueda ver el cambio de idioma en esta parte del Menu
                global langueje

                #Ejectua el fondo previamente cargado en la variable BG
                PANTALLA.blit(BG, (0, 0))
                
                #Detecta la posicion del mouse para poder interactuar con los botones
                MENU_MOUSE_POS = pygame.mouse.get_pos()

                #En una variable guardamos el texto de titulo del juego
                MENU_TEXT = get_font(100).render("SEA HEROS", True, "#b68f40")
                #Guardamos en una variable los rectangulos del texto de los botones
                MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))


                playMenu = pygame.image.load("img/Sprites/Blue-Buttons/340px/Play.png")
                playMenu1 = pygame.transform.scale(playMenu,(200,200))

                optionMenu = pygame.image.load("img/Sprites/Blue-Buttons/340px/Option.png")
                optionMenu1 = pygame.transform.scale(optionMenu,(200,200))

                noMenu = pygame.image.load("img/Sprites/Blue-Buttons/340px/No.png")
                noMenu1 = pygame.transform.scale(noMenu,(200,200))

                newPlayMenu1 = playMenu1.get_rect(topleft=(300, 250))  
                newOptionMenu1 = optionMenu1.get_rect(topleft=(500, 250))  
                newNoMenu1 = noMenu1.get_rect(topleft=(700, 250)) 

                PANTALLA.blit(playMenu1, newPlayMenu1)
                PANTALLA.blit(optionMenu1, newOptionMenu1)
                PANTALLA.blit(noMenu1, newNoMenu1)

                #Muestra en pantalla el texto y el rectangulo negro
                PANTALLA.blit(MENU_TEXT, MENU_RECT)
                
                #Evento principal para poder cerrar la ventana
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                    #Evento que detecta el mouse haga algun click
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        #Si el boton de play es presionado
                        if newPlayMenu1.collidepoint(MENU_MOUSE_POS):
                            #Entra la funcion
                            play()

                        #Si el boton de opciones es presionado
                        if newOptionMenu1.collidepoint(MENU_MOUSE_POS):
                            #Entra a la funcion
                            options()

                        #Si el boton de salir es presionado
                        if newNoMenu1.collidepoint(MENU_MOUSE_POS):
                            #Cierra todo el pygame
                            pygame.quit()
                            sys.exit()

                #Llama a la funcion de el control de musica
                ControlMusic()
                #Funcion para actualizar toda la pantalla constantemente
                pygame.display.update()
    

    #Llama al menu principal
    main_menu()

#Carga primero antes que todo la funcion de intro
intro()

