import pygame, sys, random, time
from pygame.locals import *
from button import Button
from JSON  import Load
import Menu as cfg

#Carga el nivel de sonido de musica del menu anterior en una variable temporal y lo guarda en languaje del json
SoundActual = cfg.Music

#Menu de carga de objetivos despues de dar play
def load_level1():

    #Carga el JSON
    Configuracion,langueje = Load()
    #Guarda el idioma anterior como temporal(cfg) y lo guarda en languaje del json
    langueje = cfg.idioma_actual

    #Inicia el pygame
    pygame.init()

    #Pantalla Resolucion
    W,H = 1280,720
    #Carga icono de la ventana
    icon = pygame.image.load("img/Sprites/FishAnimation/fish1.png")
    #Setea el display
    PANTALLA = pygame.display.set_mode((W,H))
    #Nombre de la ventana del juego
    pygame.display.set_caption("Sea Heroes")
    #Carga el icon
    pygame.display.set_icon(icon)

    #Carga el las imagenes en una variable
    bolsa_ico = pygame.image.load("img/Sprites/Coliders/bolsa.png")
    rock_ico = pygame.image.load("img/Sprites/Coliders/rock.png")

    #Fuentes
    font1 = pygame.font.Font('assets/upheavtt.ttf', 60)

    #Colores
    white = (255, 255, 255)
    green = (0, 208, 0)
    red = (255, 0, 0)

    #Funcion para dibujar texto en la pantalla
    def draw_text(text, font, text_col, x,y):
        img = font.render(text, True, text_col)
        PANTALLA.blit(img, (x,y))

    #Bucle para cargar el juego
    run = True
    while run:

        #Filea la pantalla en negro
        PANTALLA.fill("black")

        #Muestra el objetivo del juego
        if langueje == "es":
            draw_text(Configuracion.get(langueje, {}).get("numlevel1"), font1, white, 540, 10)
            draw_text(Configuracion.get(langueje, {}).get("object"), font1, white, 490, 200)
            draw_text(Configuracion.get(langueje, {}).get("recolet"), font1, green, 420, 310)
            PANTALLA.blit(bolsa_ico, (820, 300))
            draw_text(Configuracion.get(langueje, {}).get("evade"), font1, red, 500, 380)
            PANTALLA.blit(rock_ico, (735, 380))

        if langueje == "en":
            draw_text(Configuracion.get(langueje, {}).get("numlevel1"), font1, white, 530, 10)
            draw_text(Configuracion.get(langueje, {}).get("object"), font1, white, 470, 200)
            draw_text(Configuracion.get(langueje, {}).get("recolet"), font1, green, 450, 290)
            PANTALLA.blit(bolsa_ico, (785, 280))
            draw_text(Configuracion.get(langueje, {}).get("evade"), font1, red, 525, 360)
            PANTALLA.blit(rock_ico, (725, 360))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        pygame.display.update()

        for segundo in range(3):
            if segundo == 3:
                break
            time.sleep(1)
        
        run = False

def Level1():
        
        Configuracion,langueje = Load()
        langueje = cfg.idioma_actual

        
        #Start de pygame
        pygame.init()

        #Pantalla
        W,H = 1280,720
        icon = pygame.image.load("img/Sprites/FishAnimation/fish1.png")
        PANTALLA = pygame.display.set_mode((W,H))
        pygame.display.set_caption("Sea Heroes")
        pygame.display.set_icon(icon)

        #Fuentes
        font = pygame.font.SysFont('Bauhaus 93', 60)
        font2 = pygame.font.Font('assets/upheavtt.ttf', 40)
        font3 = pygame.font.Font('assets/upheavtt.ttf', 22)

        #Funcion para dibujar texto en la pantalla
        def draw_text(text, font, text_col, x,y):
            img = font.render(text, True, text_col)
            PANTALLA.blit(img, (x,y))
        
        #Funcion para cargar una fuente que usa para el boton de next level
        def get_font(size):
            return pygame.font.Font("assets/font.ttf", size)

        #Guarda los sonidos en una variable
        victory_sound = pygame.mixer.Sound("sound/victorysound.mp3")
        death_sound = pygame.mixer.Sound("sound/deathsound.mp3")
        recolection = pygame.mixer.Sound("sound/recolection.mp3")
        #Setea los sonidos a un volumen establecido
        victory_sound.set_volume(0.3)
        death_sound.set_volume(0.25)
        recolection.set_volume(0.5)

        #Carga las imagenes de control de volumen
        sonido_arriba = pygame.image.load("sound/img/volume_up.png")
        sonido_abajo = pygame.image.load("sound/img/volume_down.png")
        sonido_mute = pygame.image.load("sound/img/volume_muted.png")
        sonido_max = pygame.image.load("sound/img/volume_max.png")

        #Fondo en movimiento
        fondo = pygame.image.load("img/Backgrounds/Background_level1.jpg").convert()
        VelFondo = 0

        #Colores
        white = (255, 255, 255)
        black = (0, 0, 0)
        red = (255, 0, 0)

        #Variables Principales
        fps = 100
        clock = pygame.time.Clock()
        swimming = False
        game_over = False
        score = 0
        victory = False
        sound = True
        
        #Carga de imagenes de botones y el icon de objetivo
        bag_ico = pygame.image.load("img/Sprites/Icons/bolsa.png")
        gas_ico = pygame.image.load("img/Sprites/Icons/gas.png")
        flecha_up = pygame.image.load("img/Sprites/Keys/arrowup_alternative_paper.png")
        flecha_down = pygame.image.load("img/Sprites/Keys/arrowdown_alternative_paper.png")
        esc_key = pygame.image.load("img/Sprites/Keys/esc_alternative_paper.png")
        r_key = pygame.image.load("img/Sprites/Keys/r_alternative_paper.png")
        q_key = pygame.image.load("img/Sprites/Keys/q_alternative_paper.png")
        click1 = pygame.image.load("img/Sprites/Keys/mouse_L_pressed_paper.png")

        #Musica de fondo
        pygame.mixer.music.load("sound/level1.mp3")
        #Establece la musica en un bucle infinito
        pygame.mixer.music.play(-1)
        #Setea el volumen inicial de la musica
        pygame.mixer.music.set_volume == SoundActual

        #Frecuencia de aparicion de rock
        frecuencia_rock = 2300 #milisegundos
        last_rock = pygame.time.get_ticks() - frecuencia_rock

        #Frecuencia de aparicion de bolsa
        frecuencia_bag = 3000 #milisegundos
        ultima_bag = pygame.time.get_ticks() - frecuencia_bag
        
        #Defino la funcion de pausa
        def pause():
            paused = True
            while paused:
                pygame.mixer.music.pause()
                if langueje == "es":
                    draw_text(Configuracion.get(langueje, {}).get("paused"), font2, black, W / 2.3, 320)
                    draw_text(Configuracion.get(langueje, {}).get("continue"), font2, black, W / 3.5, 370)
                if langueje == "en":
                    draw_text(Configuracion.get(langueje, {}).get("paused"), font2, black, 560, 320)
                    draw_text(Configuracion.get(langueje, {}).get("continue"), font2, black, 400, 370)
                

                #evento para poder cerrar el bucle
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        paused = False
                        pygame.quit()
                        exit()
                    #si se vuelve a presionar escape
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            #reanuda el volumen y termina la pausa
                            pygame.mixer.music.unpause()
                            paused = False
                        if event.key == pygame.K_r:
                            Level1()
                        if event.key == pygame.K_q:
                            from Menu import MenuTotal
                            MenuTotal()
                        
                pygame.display.update()

        #La clase del submarino con sus atributos y funciones
        class Submarine(pygame.sprite.Sprite):
            def __init__(self, x, y):
                pygame.sprite.Sprite.__init__(self)
                self.images = []
                self.index = 0
                self.counter = 0
                for num in range (1, 4):
                    img = pygame.image.load(f"img/Sprites/Submarine/submarine{num}.png")
                    self.images.append(img)
                self.image = self.images[self.index]
                self.rect = self.image.get_rect()
                self.rect.center = [x, y]
                self.vel = 0
                self.clicked = False

            #Aqui definimos todas las actualizacion que afectan al submarino
            def update(self):
                #Gravedad del submarino
                if swimming == True:
                    self.vel += 0.5
                    if self.vel > 4:
                        self.vel = 4
                    if self.rect.bottom < 720:
                        self.rect.y += int(self.vel)

                if game_over == False:
                    #Salto del submarino
                    if pygame.mouse.get_pressed()[0] == 1 or keys[pygame.K_SPACE]:
                        self.vel = -5
                    
                    #Animaciones del submarino
                    self.counter += 1
                    flap_cooldown = 10

                    if self.counter > flap_cooldown:
                        self.counter = 0
                        self.index += 1
                        if self.index >= len(self.images):
                            self.index = 0
                    self.image = self.images[self.index]

                    #Rotacion del submarino
                    self.image = pygame.transform.rotate(self.images[self.index], self.vel * -1)
                else:
                    self.image = pygame.transform.rotate(self.images[self.index], -180)

        #La clase de la barra de combustible con sus atributos y funciones
        class FuelBar():
            def __init__(self, x, y, w, h, max_hp):
                self.x = x
                self.y = y
                self.w = w
                self.h = h
                self.hp = max_hp
                self.max_hp = max_hp

            def draw(self, surface):
                #calculate fuel ratio
                ratio = self.hp / self.max_hp
                pygame.draw.rect(surface, "#701212", (self.x, self.y, self.w, self.h))
                pygame.draw.rect(surface, "#B27313", (self.x, self.y, self.w * ratio, self.h))

        #La clase de la rock con sus atributos y funciones
        class Rock(pygame.sprite.Sprite):
            def __init__(self, x, y):
                pygame.sprite.Sprite.__init__(self)
                self.image = pygame.image.load("img/Sprites/Coliders/rock.png")
                self.rect = self.image.get_rect()
                self.rect.topleft = [x,y]
                self.image = pygame.transform.rotate(self.image, -45)

            def update(self):
                #Se quedan en su lugar al morir
                if game_over == False:
                    self.rect.x -= 2

        #La clase de la bolsa con sus atributos y funciones
        class Bag(pygame.sprite.Sprite):
            def __init__(self, x, y):
                pygame.sprite.Sprite.__init__(self)
                self.image = pygame.image.load("img/Sprites/Coliders/bolsa.png")
                self.rect = self.image.get_rect()
                self.rect.topleft = [x,y]

            def update(self):
                if game_over == False:
                    self.rect.x -= 2

        #Definimos el boton para pasar al siguiente nivel
        def ButtonNextLevel():
            PLAY_MOUSE_POS = pygame.mouse.get_pos()

            NEXT = Button(image=(None), pos=(640, 400),
                                    text_input=Configuracion.get(langueje, {}).get("buttonNext"), font=get_font(50), base_color="White", hovering_color="Green")
            NEXT.changeColor(PLAY_MOUSE_POS)
            NEXT.update(PANTALLA)

            #Bucle para cerrar el juego
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                #Evento para detectar el mouse sobre el boton y funcion de este
                if event.type == pygame.MOUSEBUTTONDOWN:
                        if NEXT.checkForInput(PLAY_MOUSE_POS):
                            load_level2()
                            Level2()

        #Funcion para imprimir las teclas en pantalla
        def keys_on_screen():
            draw_text(Configuracion.get(langueje, {}).get("keysControl"), font2, black, 1040, 380)
            PANTALLA.blit(esc_key, (1030, 410))
            draw_text(Configuracion.get(langueje, {}).get("keysPaused"), font3, black, 1100, 446)
            PANTALLA.blit(r_key, (1030, 460))
            draw_text(Configuracion.get(langueje, {}).get("keysReset"), font3, black, 1100, 490)
            PANTALLA.blit(q_key, (1030, 505))
            draw_text(Configuracion.get(langueje, {}).get("keysExit"), font3, black, 1100, 535)
            PANTALLA.blit(flecha_up, (1020, 545))
            draw_text(Configuracion.get(langueje, {}).get("keysUpMusic"), font3, black, 1100, 577)
            PANTALLA.blit(flecha_down, (1010, 580))
            draw_text(Configuracion.get(langueje, {}).get("keysDownMusic"), font3, black, 1100, 620)

        #Se declaran los objetos como grupos
        submarine_group = pygame.sprite.Group()
        rock_group = pygame.sprite.Group()
        bag_group = pygame.sprite.Group()

        #En la variable flappy almacenamos la ubicacion donde aparecera el submarino
        flappy = Submarine(100, int(H / 2))
        #Al grupo le agregamos la variable flappy
        submarine_group.add(flappy)

        #Asigna los valores a la clase vida
        fuel_bar = FuelBar(500, 35, 300, 40, 3000)
        fuel_bar.hp = 3000

        #Carga de imagenes de victoria
        images = []
        for i in range(1,5):
            name = "img/Sprites/VictoryAnimation/victory"+str(i)+".png"
            images.append(pygame.image.load(name))

        #Bucle principal del juego
        running = True
        while running:

            #Guardamos en una variable una funcion de tecla mantenida
            keys = pygame.key.get_pressed()

            #Movimiento en bucle del fondo del juego
            x_relativa = VelFondo % fondo.get_rect().width
            PANTALLA.blit(fondo,(x_relativa - fondo.get_rect().width,0))
            if x_relativa < W:
                PANTALLA.blit(fondo,(x_relativa,0))
            #Velocidad del fondo
            VelFondo -= 2
            #Velocidad del juego total
            clock.tick(fps)

            #Muestra todo en pantalla
            submarine_group.draw(PANTALLA)
            submarine_group.update()
            rock_group.draw(PANTALLA)
            rock_group.update()
            bag_group.draw(PANTALLA)
            bag_group.update()
            
            #Si la victoria todavia no esta hecha muestra el score, texto y controles
            if victory == False:
                #Muestra el score
                PANTALLA.blit(gas_ico, (420,25))
                draw_text(str(score), font, white, 1110, 20)
                draw_text(("/5"), font, white, 1150, 20) 
                PANTALLA.blit(bag_ico, (1220,20))
                fuel_bar.draw(PANTALLA)
                if langueje == "en":
                    draw_text(Configuracion.get(langueje, {}).get("fuel"), font2, black, 610, 0)
                elif langueje == "es":
                    draw_text(Configuracion.get(langueje, {}).get("fuel"), font2, black, 520, 0)
                

            
            #Cuando empizas el juego empieza muestra instrucciones
            if swimming == False and game_over == False:
                draw_text(Configuracion.get(langueje, {}).get("swimming"), font2, black, 400, 340)
                PANTALLA.blit(click1, (588, 315))
                #Funcion que muestre las teclas
                keys_on_screen()
            
            #Revisa que el submarino no se salga del agua
            if flappy.rect.top < 200:
                flappy.rect.top = 200
            
            #Revisa la colision del submarino con la roca
            if pygame.sprite.groupcollide(submarine_group, rock_group, False, False):
                game_over = True
    
            #Revisa la colision del submarino con la bolsa
            hits = pygame.sprite.groupcollide(submarine_group, bag_group, False, True)

            #bucle donde se van sumando los puntos por colisiones
            for hit in hits:
                score += 1
                recolection.play()

            #Defino la funcion de los controles de volumen
            def AudioControl():
                if keys[pygame.K_DOWN] and pygame.mixer_music.get_volume() > 0.0:
                    pygame.mixer.music.set_volume(pygame.mixer_music.get_volume() - 0.01)
                    PANTALLA.blit(sonido_abajo, (1150,25))
                elif keys[pygame.K_DOWN] and pygame.mixer_music.get_volume() == 0.0:
                    PANTALLA.blit(sonido_mute, (1150,25))

                #Sube volumen
                if keys[pygame.K_UP] and pygame.mixer_music.get_volume() < 1.0:
                    pygame.mixer.music.set_volume(pygame.mixer_music.get_volume() + 0.01)
                    PANTALLA.blit(sonido_arriba, (1150,25))
                elif keys[pygame.K_UP] and pygame.mixer_music.get_volume() == 1.0:
                    PANTALLA.blit(sonido_max, (1150,25))

            #Detecta si el jugador gana
            if score == 5 and game_over == False:
                victory = True
                def WinScreen():
                    #Se limpia todos los objetos
                    rock_group.empty()
                    bag_group.empty()
                    submarine_group.empty()
                    #Muestra la imagen de victoria animada
                    frame = int(time.time()*10) % 4
                    PANTALLA.blit(images[frame], (0, 0))
                    #Muestra el boton de next
                    ButtonNextLevel()
                    #Se detiene la musica
                    pygame.mixer.music.stop()
                    for sound in hits:
                        victory_sound.play()
                WinScreen()

            #Revisa que el submarino toque el suelo
            if flappy.rect.bottom >= 720:
                game_over = True
                swimming = False
                
            #Checa que el juego no llegue a Game Over
            if game_over == False and swimming == True:
                #Generador de roca
                time_now = pygame.time.get_ticks()
                if time_now - last_rock > frecuencia_rock:
                    rock_spawn = random.randint(200, 600)
                    rock = Rock(W, + rock_spawn)
                    rock_group.add(rock)
                    last_rock = time_now

            #Checa que el juego no llegue a Game Over
            if game_over == False and swimming == True:
                #Generador de bolsa
                time_now = pygame.time.get_ticks()
                if time_now - ultima_bag > frecuencia_bag:
                    bag_spawn = random.randint(200, 600)
                    bag = Bag(W, + bag_spawn)
                    bag_group.add(bag)
                    ultima_bag = time_now

            #Checa que el juego llegue a GameOver y dibuja los botones
            if game_over == True:
                pygame.mixer.music.stop()
                score = 0
                VelFondo = 0
                if langueje == "es":
                    draw_text(Configuracion.get(langueje, {}).get("overReset"), font2, black, W / 3.5, 330)
                    draw_text(Configuracion.get(langueje, {}).get("overExit"), font2, black, W / 3.1, 380)
                    draw_text(Configuracion.get(langueje, {}).get("teaching"), font2, red, 500, 250)
                    PANTALLA.blit(r_key, (490, 310))
                    PANTALLA.blit(q_key, (535, 360))
                if langueje == "en":
                    draw_text(Configuracion.get(langueje, {}).get("overReset"), font2, black, 450, 330)
                    draw_text(Configuracion.get(langueje, {}).get("overExit"), font2, black, 500, 380)
                    draw_text(Configuracion.get(langueje, {}).get("teaching"), font2, red, 550, 250)
                    PANTALLA.blit(r_key, (575, 310))
                    PANTALLA.blit(q_key, (625, 360))
                
            #Si el jugador muere reproduce el sonido
            if game_over == True and sound == True:
                death_sound.play()
                #La variable la vuelve falsa para que el if no se cumpla y no reproduzca en bucle
                sound = False

            #El decremento de la vida si el jugador empieza a jugar
            if swimming == True and game_over == False and victory == False:
                fuel_bar.hp -= 1
                if fuel_bar.hp <= 0:
                    game_over = True
                    death_sound.play()
                    
                        

            #Evento para poder cerrar la ventana del juego y no se quede en bucle infinito
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                    pygame.quit()
                    exit()
                #Detecta que el juego empiece al clickear
                if event.type == pygame.MOUSEBUTTONDOWN and swimming == False and game_over == False:
                    swimming = True
                #Detecta que el juego empiece al presionar space
                if event.type == pygame.KEYDOWN and swimming == False and game_over == False:
                    if event.key == pygame.K_SPACE:
                        swimming = True
                #Evento para detectar una pulsacion de tecla
                if event.type == pygame.KEYDOWN:
                    #Si la tecla presionada es Escape y el juego ya empezo
                    if event.key == pygame.K_ESCAPE and game_over == False and swimming == True:
                        if langueje == "es":
                            PANTALLA.blit(esc_key, (495, 345))
                        if langueje == "en":
                            PANTALLA.blit(esc_key, (530, 345))
                        keys_on_screen()
                        #Se va la funcion pause que es un bucle while
                        pause()
                    if event.key == pygame.K_r:
                        Level1()
                    if event.key == pygame.K_q:
                        pygame.mixer.music.stop()
                        #Carga el menu
                        from Menu import MenuTotal
                        MenuTotal()
                        
            #Carga el control de audio cuando carga el nivel            
            AudioControl()
            #Funcion para actualizar la pantalla constantemente
            pygame.display.update()

def load_level2():

    #Carga el JSON
    Configuracion,langueje = Load()
    #Guarda el idioma anterior como temporal(cfg) y lo guarda en languaje del json
    langueje = cfg.idioma_actual

    #Inicia el pygame
    pygame.init()

    #Pantalla Resolucion
    W,H = 1280,720
    #Carga icono de la ventana
    icon = pygame.image.load("img/Sprites/FishAnimation/fish1.png")
    #Setea el display
    PANTALLA = pygame.display.set_mode((W,H))
    #Nombre de la ventana del juego
    pygame.display.set_caption("Sea Heroes")
    #Carga el icon
    pygame.display.set_icon(icon)

    #Carga el las imagenes en una variable
    bottle_ico = pygame.image.load("img/Sprites/Icons/botella.png")
    rock_ico = pygame.image.load("img/Sprites/Coliders/rock.png")
    fish_ico = pygame.image.load("img/Sprites/FishAnimation/fish1.png")

    #Fuentes
    font1 = pygame.font.Font('assets/upheavtt.ttf', 60)

    #Colores
    white = (255, 255, 255)
    green = (0, 208, 0)
    red = (255, 0, 0)

    #Funcion para dibujar texto en la pantalla
    def draw_text(text, font, text_col, x,y):
        img = font.render(text, True, text_col)
        PANTALLA.blit(img, (x,y))

    #Bucle para cargar el juego
    run = True
    while run:

        #Filea la pantalla en negro
        PANTALLA.fill("black")

        #Muestra el objetivo del juego
        if langueje == "es":
            draw_text(Configuracion.get(langueje, {}).get("numlevel2"), font1, white, 540, 10)
            draw_text(Configuracion.get(langueje, {}).get("object"), font1, white, 490, 200)
            draw_text(Configuracion.get(langueje, {}).get("save"), font1, green, 450, 310)
            PANTALLA.blit(fish_ico, (750, 305))
            draw_text(Configuracion.get(langueje, {}).get("evade"), font1, red, 450, 380)
            PANTALLA.blit(rock_ico, (735, 380))
            PANTALLA.blit(bottle_ico, (680, 380))

        if langueje == "en":
            draw_text(Configuracion.get(langueje, {}).get("numlevel2"), font1, white, 530, 10)
            draw_text(Configuracion.get(langueje, {}).get("object"), font1, white, 470, 200)
            draw_text(Configuracion.get(langueje, {}).get("save"), font1, green, 480, 290)
            PANTALLA.blit(fish_ico, (710, 290))
            draw_text(Configuracion.get(langueje, {}).get("evade"), font1, red, 480, 360)
            PANTALLA.blit(rock_ico, (750, 355))
            PANTALLA.blit(bottle_ico, (680, 350))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        pygame.display.update()

        for segundo in range(3):
            if segundo == 3:
                break
            time.sleep(1)
        
        run = False

def Level2():
        
        Configuracion,langueje = Load()
        langueje = cfg.idioma_actual

        
        #Start de pygame
        pygame.init()

        #Pantalla
        W,H = 1280,720
        icon = pygame.image.load("img/Sprites/FishAnimation/fish1.png")
        PANTALLA = pygame.display.set_mode((W,H))
        pygame.display.set_caption("Sea Heroes")
        pygame.display.set_icon(icon)

        #Fuentes
        font = pygame.font.SysFont('Bauhaus 93', 60)
        font2 = pygame.font.Font('assets/upheavtt.ttf', 40)
        font3 = pygame.font.Font('assets/upheavtt.ttf', 22)

        #Funcion para dibujar texto en la pantalla
        def draw_text(text, font, text_col, x,y):
            img = font.render(text, True, text_col)
            PANTALLA.blit(img, (x,y))
        
        #Funcion para cargar una fuente que usa para el boton de next level
        def get_font(size):
            return pygame.font.Font("assets/font.ttf", size)

        #Guarda los sonidos en una variable
        victory_sound = pygame.mixer.Sound("sound/victorysound.mp3")
        death_sound = pygame.mixer.Sound("sound/deathsound.mp3")
        recolection = pygame.mixer.Sound("sound/recolection.mp3")
        #Setea los sonidos a un volumen establecido
        victory_sound.set_volume(0.3)
        death_sound.set_volume(0.25)
        recolection.set_volume(0.5)

        #Carga las imagenes de control de volumen
        sonido_arriba = pygame.image.load("sound/img/volume_up.png")
        sonido_abajo = pygame.image.load("sound/img/volume_down.png")
        sonido_mute = pygame.image.load("sound/img/volume_muted.png")
        sonido_max = pygame.image.load("sound/img/volume_max.png")

        #Fondo en movimiento
        fondo = pygame.image.load("img/Backgrounds/Background_level2.png").convert()
        VelFondo = 0

        #Colores
        white = (255, 255, 255)
        black = (0, 0, 0)
        red = (255, 0, 0)

        #Variables Principales
        fps = 100
        clock = pygame.time.Clock()
        swimming = False
        game_over = False
        score = 0
        victory = False
        sound = True
        
        #Carga de imagenes de botones y el icon de objetivo
        fish_ico = pygame.image.load("img/Sprites/Icons/fish.png")
        oxygen_ico = pygame.image.load("img/Sprites/Icons/oxygen.png")
        flecha_up = pygame.image.load("img/Sprites/Keys/arrowup_alternative_paper.png")
        flecha_down = pygame.image.load("img/Sprites/Keys/arrowdown_alternative_paper.png")
        esc_key = pygame.image.load("img/Sprites/Keys/esc_alternative_paper.png")
        r_key = pygame.image.load("img/Sprites/Keys/r_alternative_paper.png")
        q_key = pygame.image.load("img/Sprites/Keys/q_alternative_paper.png")
        click1 = pygame.image.load("img/Sprites/Keys/mouse_L_pressed_paper.png")

        #Musica de fondo
        pygame.mixer.music.load("sound/level2.mp3")
        #Establece la musica en un bucle infinito
        pygame.mixer.music.play(-1)
        #Setea el volumen inicial de la musica
        pygame.mixer.music.set_volume == SoundActual

        #Frecuencia de aparicion de rock
        frecuencia_rock = 2300 #milisegundos
        last_rock = pygame.time.get_ticks() - frecuencia_rock

        #Frecuencia de aparicion de botella
        frecuencia_bottle = 2700
        last_bottle = pygame.time.get_ticks() - frecuencia_bottle

        #Frecuencia de aparicion de pescado atrapado
        frecuencia_pez = 5000 #milisegundos
        ultimo_pez = pygame.time.get_ticks() - frecuencia_pez + 1000
        
        #Defino la funcion de pausa
        def pause():
            paused = True
            while paused:
                pygame.mixer.music.pause()
                if langueje == "es":
                    draw_text(Configuracion.get(langueje, {}).get("paused"), font2, black, W / 2.3, 320)
                    draw_text(Configuracion.get(langueje, {}).get("continue"), font2, black, W / 3.5, 370)
                if langueje == "en":
                    draw_text(Configuracion.get(langueje, {}).get("paused"), font2, black, 560, 320)
                    draw_text(Configuracion.get(langueje, {}).get("continue"), font2, black, 400, 370)
                

                #evento para poder cerrar el bucle
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        paused = False
                        pygame.quit()
                        exit()
                    #si se vuelve a presionar escape
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            #reanuda el volumen y termina la pausa
                            pygame.mixer.music.unpause()
                            paused = False
                        if event.key == pygame.K_r:
                            Level1()
                        if event.key == pygame.K_q:
                            from Menu import MenuTotal
                            MenuTotal()
                        
                pygame.display.update()

        #La clase del submarino con sus atributos y funciones
        class Buzo(pygame.sprite.Sprite):
            def __init__(self, x, y):
                pygame.sprite.Sprite.__init__(self)
                self.images = []
                self.index = 0
                self.counter = 0
                for num in range (1, 5):
                    img = pygame.image.load(f"img/Sprites/Buzo/buzo{num}.png")
                    self.images.append(img)
                self.image = self.images[self.index]
                self.rect = self.image.get_rect()
                self.rect.center = [x, y]
                self.vel = 0

            #Aqui definimos todas las actualizacion que afectan al submarino
            def update(self):
                #Gravedad del submarino
                if swimming == True:
                    self.vel += 0.5
                    if self.vel > 4:
                        self.vel = 4
                    if self.rect.bottom < 900:
                        self.rect.y += int(self.vel)

                if game_over == False:
                    #Salto del submarino
                    if pygame.mouse.get_pressed()[0] == 1 or keys[pygame.K_SPACE]:
                        self.vel = -5

                    
                    #Animaciones del submarino
                    self.counter += 1
                    flap_cooldown = 10

                    if self.counter > flap_cooldown:
                        self.counter = 0
                        self.index += 1
                        if self.index >= len(self.images):
                            self.index = 0
                    self.image = self.images[self.index]

                    #Rotacion del submarino
                    self.image = pygame.transform.rotate(self.images[self.index], self.vel * -1)
                else:
                    self.image = pygame.transform.rotate(self.images[self.index], -90)

        #La clase de la barra de combustible con sus atributos y funciones
        class FuelBar():
            def __init__(self, x, y, w, h, max_hp):
                self.x = x
                self.y = y
                self.w = w
                self.h = h
                self.hp = max_hp
                self.max_hp = max_hp

            def draw(self, surface):
                #calculate fuel ratio
                ratio = self.hp / self.max_hp
                pygame.draw.rect(surface, "#FF0000", (self.x, self.y, self.w, self.h))
                pygame.draw.rect(surface, "Blue", (self.x, self.y, self.w * ratio, self.h))

        #La clase de la rock con sus atributos y funciones
        class Rock(pygame.sprite.Sprite):
            def __init__(self, x, y):
                pygame.sprite.Sprite.__init__(self)
                self.image = pygame.image.load("img/Sprites/Coliders/rock.png")
                self.rect = self.image.get_rect()
                self.rect.topleft = [x,y]
                self.image = pygame.transform.rotate(self.image, -45)

            def update(self):
                #Se quedan en su lugar al morir
                if game_over == False:
                    self.rect.x -= 2

        #La clase de la rock con sus atributos y funciones
        class Bottle(pygame.sprite.Sprite):
            def __init__(self, x, y):
                pygame.sprite.Sprite.__init__(self)
                self.image = pygame.image.load("img/Sprites/Coliders/botella.png")
                self.rect = self.image.get_rect()
                self.rect.topleft = [x,y]

            def update(self):
                #Se quedan en su lugar al morir
                if game_over == False:
                    self.rect.x -= 2

        #La clase de la bolsa con sus atributos y funciones
        class FishTraped(pygame.sprite.Sprite):
            def __init__(self, x, y):
                pygame.sprite.Sprite.__init__(self)
                self.image = pygame.image.load("img/Sprites/FishAnimation/pez_atrapado.png")
                self.rect = self.image.get_rect()
                self.rect.topleft = [x,y]

            def update(self):
                if game_over == False:
                    self.rect.x -= 2

        #Definimos el boton para pasar al siguiente nivel
        def ButtonNextLevel():
            PLAY_MOUSE_POS = pygame.mouse.get_pos()

            NEXT = Button(image=(None), pos=(640, 400),
                                    text_input=Configuracion.get(langueje, {}).get("buttonNext"), font=get_font(50), base_color="White", hovering_color="Green")
            NEXT.changeColor(PLAY_MOUSE_POS)
            NEXT.update(PANTALLA)

            #Bucle para cerrar el juego
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                #Evento para detectar el mouse sobre el boton y funcion de este
                if event.type == pygame.MOUSEBUTTONDOWN:
                        if NEXT.checkForInput(PLAY_MOUSE_POS):
                            Level3()

        #Funcion para imprimir las teclas en pantalla
        def keys_on_screen():
            draw_text(Configuracion.get(langueje, {}).get("keysControl"), font2, black, 1040, 380)
            PANTALLA.blit(esc_key, (1030, 410))
            draw_text(Configuracion.get(langueje, {}).get("keysPaused"), font3, black, 1100, 446)
            PANTALLA.blit(r_key, (1030, 460))
            draw_text(Configuracion.get(langueje, {}).get("keysReset"), font3, black, 1100, 490)
            PANTALLA.blit(q_key, (1030, 505))
            draw_text(Configuracion.get(langueje, {}).get("keysExit"), font3, black, 1100, 535)
            PANTALLA.blit(flecha_up, (1020, 545))
            draw_text(Configuracion.get(langueje, {}).get("keysUpMusic"), font3, black, 1100, 577)
            PANTALLA.blit(flecha_down, (1010, 580))
            draw_text(Configuracion.get(langueje, {}).get("keysDownMusic"), font3, black, 1100, 620)

        #Se declaran los objetos como grupos
        submarine_group = pygame.sprite.Group()
        rock_group = pygame.sprite.Group()
        pez_group = pygame.sprite.Group()
        bottle_group = pygame.sprite.Group()

        #En la variable flappy almacenamos la ubicacion donde aparecera el buzo
        flappy = Buzo(100, int(H / 2))
        #Al grupo le agregamos la variable flappy
        submarine_group.add(flappy)

        #Asigna los valores a la clase vida
        fuel_bar = FuelBar(500, 35, 300, 40, 5000)
        fuel_bar.hp = 5000

        #Carga de imagenes de victoria
        images = []
        for i in range(1,5):
            name = "img/Sprites/VictoryAnimation/victory"+str(i)+".png"
            images.append(pygame.image.load(name))

        #Bucle principal del juego
        running = True
        while running:

            #Guardamos en una variable una funcion de tecla mantenida
            keys = pygame.key.get_pressed()

            #Movimiento en bucle del fondo del juego
            x_relativa = VelFondo % fondo.get_rect().width
            PANTALLA.blit(fondo,(x_relativa - fondo.get_rect().width,0))
            if x_relativa < W:
                PANTALLA.blit(fondo,(x_relativa,0))
            #Velocidad del fondo
            VelFondo -= 2
            #Velocidad del juego total
            clock.tick(fps)

            #Muestra todo en pantalla
            submarine_group.draw(PANTALLA)
            submarine_group.update()
            rock_group.draw(PANTALLA)
            rock_group.update()
            pez_group.draw(PANTALLA)
            pez_group.update()
            bottle_group.draw(PANTALLA)
            bottle_group.update()
            
            #Si la victoria todavia no esta hecha muestra el score, texto y controles
            if victory == False:
                #Muestra el score
                PANTALLA.blit(oxygen_ico, (450,15))
                draw_text(str(score), font, white, 1100, 20)
                draw_text(("/7"), font, white, 1130, 20) 
                PANTALLA.blit(fish_ico, (1190,25))
                fuel_bar.draw(PANTALLA)
                if langueje == "en":
                    draw_text(Configuracion.get(langueje, {}).get("oxigen"), font2, black, 575, 0)
                elif langueje == "es":
                    draw_text(Configuracion.get(langueje, {}).get("oxigen"), font2, black, 570, 0)
                

            
            #Cuando empizas el juego empieza muestra instrucciones
            if swimming == False and game_over == False:
                draw_text(Configuracion.get(langueje, {}).get("swimming"), font2, black, 400, 340)
                PANTALLA.blit(click1, (588, 315))
                #Funcion que muestre las teclas
                keys_on_screen()
            
            #Revisa que el submarino no se salga del agua
            if flappy.rect.top < 0:
                flappy.rect.top = 0
            
            #Revisa la colision del submarino con la roca
            if pygame.sprite.groupcollide(submarine_group, rock_group, False, False):
                game_over = True
            if pygame.sprite.groupcollide(submarine_group, bottle_group, False, False):
                game_over = True
    
            #Revisa la colision del submarino con el pez
            hits = pygame.sprite.groupcollide(submarine_group, pez_group, False, True)

            #bucle donde se van sumando los puntos por colisiones
            for hit in hits:
                score += 1
                recolection.play()

            #Defino la funcion de los controles de volumen
            def AudioControl():
                if keys[pygame.K_DOWN] and pygame.mixer_music.get_volume() > 0.0:
                    pygame.mixer.music.set_volume(pygame.mixer_music.get_volume() - 0.01)
                    PANTALLA.blit(sonido_abajo, (1150,25))
                elif keys[pygame.K_DOWN] and pygame.mixer_music.get_volume() == 0.0:
                    PANTALLA.blit(sonido_mute, (1150,25))

                #Sube volumen
                if keys[pygame.K_UP] and pygame.mixer_music.get_volume() < 1.0:
                    pygame.mixer.music.set_volume(pygame.mixer_music.get_volume() + 0.01)
                    PANTALLA.blit(sonido_arriba, (1150,25))
                elif keys[pygame.K_UP] and pygame.mixer_music.get_volume() == 1.0:
                    PANTALLA.blit(sonido_max, (1150,25))

            #Detecta si el jugador gana
            if score == 7 and game_over == False:
                victory = True
                def WinScreen():
                    #Se limpia todos los objetos
                    rock_group.empty()
                    pez_group.empty()
                    submarine_group.empty()
                    bottle_group.empty()
                    #Muestra la imagen de victoria animada
                    frame = int(time.time()*10) % 4
                    PANTALLA.blit(images[frame], (0, 0))
                    #Muestra el boton de next
                    ButtonNextLevel()
                    #Se detiene la musica
                    pygame.mixer.music.stop()
                    for sound in hits:
                        victory_sound.play()
                WinScreen()

            #Revisa que el submarino toque el suelo
            if flappy.rect.bottom >= 800:
                game_over = True
                swimming = False
                
                

            #Checa que el juego no llegue a Game Over
            if game_over == False and swimming == True:
                #Generador de roca
                time_now = pygame.time.get_ticks()
                if time_now - last_rock > frecuencia_rock:
                    rock_spawn = random.randint(100, 600)
                    rock = Rock(W, + rock_spawn)
                    rock_group.add(rock)
                    last_rock = time_now
            
            #Checa que el juego no llegue a Game Over
            if game_over == False and swimming == True:
                #Generador de botella
                time_now = pygame.time.get_ticks()
                if time_now - last_bottle > frecuencia_bottle:
                    bottle_spawn = random.randint(-100, 200)
                    bottle = Bottle(W, int(H / 2) + bottle_spawn)
                    bottle_group.add(bottle)
                    last_bottle = time_now

            #Checa que el juego no llegue a Game Over
            if game_over == False and swimming == True:
                #Generador de pescado
                time_now = pygame.time.get_ticks()
                if time_now - ultimo_pez > frecuencia_pez:
                    pez_spawn = random.randint(100, 600)
                    pez = FishTraped(W, + pez_spawn)
                    pez_group.add(pez)
                    ultimo_pez = time_now

            #Checa que el juego llegue a GameOver y dibuja los botones
            if game_over == True:
                pygame.mixer.music.stop()
                score = 0
                VelFondo = 0
                if langueje == "es":
                    draw_text(Configuracion.get(langueje, {}).get("overReset"), font2, black, W / 3.5, 330)
                    draw_text(Configuracion.get(langueje, {}).get("overExit"), font2, black, W / 3.1, 380)
                    draw_text(Configuracion.get(langueje, {}).get("teaching"), font2, red, 500, 250)
                    PANTALLA.blit(r_key, (490, 310))
                    PANTALLA.blit(q_key, (535, 360))
                if langueje == "en":
                    draw_text(Configuracion.get(langueje, {}).get("overReset"), font2, black, 450, 330)
                    draw_text(Configuracion.get(langueje, {}).get("overExit"), font2, black, 500, 380)
                    draw_text(Configuracion.get(langueje, {}).get("teaching"), font2, red, 550, 250)
                    PANTALLA.blit(r_key, (575, 310))
                    PANTALLA.blit(q_key, (625, 360))
                
            #Si el jugador muere reproduce el sonido
            if game_over == True and sound == True:
                death_sound.play()
                #La variable la vuelve falsa para que el if no se cumpla y no reproduzca en bucle
                sound = False

            #El decremento de la vida si el jugador empieza a jugar
            if swimming == True and game_over == False and victory == False:
                fuel_bar.hp -= 1
                if fuel_bar.hp <= 0:
                    game_over = True
                    death_sound.play()
                    
                        

            #Evento para poder cerrar la ventana del juego y no se quede en bucle infinito
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                    pygame.quit()
                    exit()
                #Detecta que el juego empiece al clickear
                if event.type == pygame.MOUSEBUTTONDOWN and swimming == False and game_over == False:
                    swimming = True
                #Detecta que el juego empiece al presionar space
                if event.type == pygame.KEYDOWN and swimming == False and game_over == False:
                    if event.key == pygame.K_SPACE:
                        swimming = True
                #Evento para detectar una pulsacion de tecla
                if event.type == pygame.KEYDOWN:
                    #Si la tecla presionada es Escape y el juego ya empezo
                    if event.key == pygame.K_ESCAPE and game_over == False and swimming == True:
                        if langueje == "es":
                            PANTALLA.blit(esc_key, (495, 345))
                        if langueje == "en":
                            PANTALLA.blit(esc_key, (530, 345))
                        keys_on_screen()
                        #Se va la funcion pause que es un bucle while
                        pause()
                    if event.key == pygame.K_r:
                        Level2()
                    if event.key == pygame.K_q:
                        pygame.mixer.music.stop()
                        #Carga el menu
                        from Menu import MenuTotal
                        MenuTotal()
                        
            #Carga el control de audio cuando carga el nivel            
            AudioControl()
            #Funcion para actualizar la pantalla constantemente
            pygame.display.update()

def load_level3():

    #Carga el JSON
    Configuracion,langueje = Load()
    #Guarda el idioma anterior como temporal(cfg) y lo guarda en languaje del json
    langueje = cfg.idioma_actual

    #Inicia el pygame
    pygame.init()

    #Pantalla Resolucion
    W,H = 1280,720
    #Carga icono de la ventana
    icon = pygame.image.load("img/Sprites/FishAnimation/fish1.png")
    #Setea el display
    PANTALLA = pygame.display.set_mode((W,H))
    #Nombre de la ventana del juego
    pygame.display.set_caption("Sea Heroes")
    #Carga el icon
    pygame.display.set_icon(icon)

    #Carga el las imagenes en una variable
    bottle_ico = pygame.image.load("img/Sprites/Icons/botella.png")
    rock_ico = pygame.image.load("img/Sprites/Coliders/rock.png")
    fish_ico = pygame.image.load("img/Sprites/FishAnimation/fish1.png")
    bolsa_ico = pygame.image.load("img/Sprites/Coliders/bolsa.png")

    #Fuentes
    font1 = pygame.font.Font('assets/upheavtt.ttf', 60)

    #Colores
    white = (255, 255, 255)
    green = (0, 208, 0)
    red = (255, 0, 0)

    #Funcion para dibujar texto en la pantalla
    def draw_text(text, font, text_col, x,y):
        img = font.render(text, True, text_col)
        PANTALLA.blit(img, (x,y))

    #Bucle para cargar el juego
    run = True
    while run:

        #Filea la pantalla en negro
        PANTALLA.fill("black")

        #Muestra el objetivo del juego
        if langueje == "es":
            draw_text(Configuracion.get(langueje, {}).get("numlevel3"), font1, white, 540, 10)
            draw_text(Configuracion.get(langueje, {}).get("object"), font1, white, 490, 200)
            draw_text(Configuracion.get(langueje, {}).get("save"), font1, green, 450, 310)
            PANTALLA.blit(fish_ico, (750, 305))
            draw_text(Configuracion.get(langueje, {}).get("recolet"), font1, green, 450, 370)
            PANTALLA.blit(bolsa_ico, (850, 360))
            draw_text(Configuracion.get(langueje, {}).get("evade"), font1, red, 450, 430)
            PANTALLA.blit(rock_ico, (735, 430))
            PANTALLA.blit(bottle_ico, (680, 430))

        if langueje == "en":
            draw_text(Configuracion.get(langueje, {}).get("numlevel3"), font1, white, 540, 10)
            draw_text(Configuracion.get(langueje, {}).get("object"), font1, white, 490, 200)
            draw_text(Configuracion.get(langueje, {}).get("save"), font1, green, 500, 310)
            PANTALLA.blit(fish_ico, (710, 310))
            draw_text(Configuracion.get(langueje, {}).get("recolet"), font1, green, 450, 370)
            PANTALLA.blit(bolsa_ico, (780, 360))
            draw_text(Configuracion.get(langueje, {}).get("evade"), font1, red, 480, 430)
            PANTALLA.blit(rock_ico, (735, 430))
            PANTALLA.blit(bottle_ico, (680, 430))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        pygame.display.update()

        for segundo in range(3):
            if segundo == 3:
                break
            time.sleep(1)
        
        run = False

def Level3():
        
        Configuracion,langueje = Load()
        langueje = cfg.idioma_actual

        
        #Start de pygame
        pygame.init()

        #Pantalla
        W,H = 1280,720
        icon = pygame.image.load("img/Sprites/FishAnimation/fish1.png")
        PANTALLA = pygame.display.set_mode((W,H))
        pygame.display.set_caption("Sea Heroes")
        pygame.display.set_icon(icon)

        #Fuentes
        font = pygame.font.SysFont('Bauhaus 93', 60)
        font2 = pygame.font.Font('assets/upheavtt.ttf', 40)
        font3 = pygame.font.Font('assets/upheavtt.ttf', 22)

        #Funcion para dibujar texto en la pantalla
        def draw_text(text, font, text_col, x,y):
            img = font.render(text, True, text_col)
            PANTALLA.blit(img, (x,y))
        
        #Funcion para cargar una fuente que usa para el boton de next level
        def get_font(size):
            return pygame.font.Font("assets/font.ttf", size)

        #Guarda los sonidos en una variable
        victory_sound = pygame.mixer.Sound("sound/victorysound.mp3")
        death_sound = pygame.mixer.Sound("sound/deathsound.mp3")
        recolection = pygame.mixer.Sound("sound/recolection.mp3")
        #Setea los sonidos a un volumen establecido
        victory_sound.set_volume(0.3)
        death_sound.set_volume(0.25)
        recolection.set_volume(0.5)

        #Carga las imagenes de control de volumen
        sonido_arriba = pygame.image.load("sound/img/volume_up.png")
        sonido_abajo = pygame.image.load("sound/img/volume_down.png")
        sonido_mute = pygame.image.load("sound/img/volume_muted.png")
        sonido_max = pygame.image.load("sound/img/volume_max.png")

        #Fondo en movimiento
        fondo = pygame.image.load("img/Backgrounds/Background_level3.png").convert()
        VelFondo = 0

        #Colores
        white = (255, 255, 255)
        black = (0, 0, 0)
        red = (255, 0, 0)

        #Variables Principales
        fps = 100
        clock = pygame.time.Clock()
        swimming = False
        game_over = False
        score = 0
        score2 = 0
        victory = False
        sound = True
        
        #Carga de imagenes de botones y el icon de objetivo
        bag_ico = pygame.image.load("img/Sprites/Icons/bolsa.png")
        fish_ico = pygame.image.load("img/Sprites/Icons/fish.png")
        oxygen_ico = pygame.image.load("img/Sprites/Icons/oxygen.png")
        flecha_up = pygame.image.load("img/Sprites/Keys/arrowup_alternative_paper.png")
        flecha_down = pygame.image.load("img/Sprites/Keys/arrowdown_alternative_paper.png")
        esc_key = pygame.image.load("img/Sprites/Keys/esc_alternative_paper.png")
        r_key = pygame.image.load("img/Sprites/Keys/r_alternative_paper.png")
        q_key = pygame.image.load("img/Sprites/Keys/q_alternative_paper.png")
        click1 = pygame.image.load("img/Sprites/Keys/mouse_L_pressed_paper.png")

        #Musica de fondo
        pygame.mixer.music.load("sound/psykick-112469.mp3")
        #Establece la musica en un bucle infinito
        pygame.mixer.music.play(-1)
        #Setea el volumen inicial de la musica
        pygame.mixer.music.set_volume == SoundActual

        #Frecuencia de aparicion de rock
        frecuencia_rock = 2300 #milisegundos
        last_rock = pygame.time.get_ticks() - frecuencia_rock + 1000

        #Frecuencia de aparicion de botella
        frecuencia_bottle = 2700
        last_bottle = pygame.time.get_ticks() - frecuencia_bottle + 1500

        #Frecuencia de aparicion de pescado atrapado
        frecuencia_pez = 5000 #milisegundos
        ultimo_pez = pygame.time.get_ticks() - frecuencia_pez + 500

        #Frecuencia de aparicion de bolsa
        frecuencia_bag = 3200 #milisegundos
        ultima_bag = pygame.time.get_ticks() - frecuencia_bag
        
        #Defino la funcion de pausa
        def pause():
            paused = True
            while paused:
                pygame.mixer.music.pause()
                if langueje == "es":
                    draw_text(Configuracion.get(langueje, {}).get("paused"), font2, black, W / 2.3, 320)
                    draw_text(Configuracion.get(langueje, {}).get("continue"), font2, black, W / 3.5, 370)
                if langueje == "en":
                    draw_text(Configuracion.get(langueje, {}).get("paused"), font2, black, 560, 320)
                    draw_text(Configuracion.get(langueje, {}).get("continue"), font2, black, 400, 370)
                

                #evento para poder cerrar el bucle
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        paused = False
                        pygame.quit()
                        exit()
                    #si se vuelve a presionar escape
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            #reanuda el volumen y termina la pausa
                            pygame.mixer.music.unpause()
                            paused = False
                        if event.key == pygame.K_r:
                            Level1()
                        if event.key == pygame.K_q:
                            from Menu import MenuTotal
                            MenuTotal()
                        
                pygame.display.update()

        #La clase del submarino con sus atributos y funciones
        class DelfinBuzo(pygame.sprite.Sprite):
            def __init__(self, x, y):
                pygame.sprite.Sprite.__init__(self)
                self.images = []
                self.index = 0
                self.counter = 0
                for num in range (1, 5):
                    img = pygame.image.load(f"img/Sprites/DelfinBuzo/delbuzo{num}.png")
                    self.images.append(img)
                self.image = self.images[self.index]
                self.rect = self.image.get_rect()
                self.rect.center = [x, y]
                self.vel = 0

            #Aqui definimos todas las actualizacion que afectan al submarino
            def update(self):
                #Gravedad del submarino
                if swimming == True:
                    self.vel += 0.5
                    if self.vel > 4:
                        self.vel = 4
                    if self.rect.bottom < 900:
                        self.rect.y += int(self.vel)

                if game_over == False:
                    #Salto del submarino
                    if pygame.mouse.get_pressed()[0] == 1 or keys[pygame.K_SPACE]:
                        self.vel = -5

                    
                    #Animaciones del submarino
                    self.counter += 1
                    flap_cooldown = 10

                    if self.counter > flap_cooldown:
                        self.counter = 0
                        self.index += 1
                        if self.index >= len(self.images):
                            self.index = 0
                    self.image = self.images[self.index]

                    #Rotacion del submarino
                    self.image = pygame.transform.rotate(self.images[self.index], self.vel * -1)
                else:
                    self.image = pygame.transform.rotate(self.images[self.index], -90)

        #La clase de la barra de combustible con sus atributos y funciones
        class FuelBar():
            def __init__(self, x, y, w, h, max_hp):
                self.x = x
                self.y = y
                self.w = w
                self.h = h
                self.hp = max_hp
                self.max_hp = max_hp

            def draw(self, surface):
                #calculate fuel ratio
                ratio = self.hp / self.max_hp
                pygame.draw.rect(surface, "Red", (self.x, self.y, self.w, self.h))
                pygame.draw.rect(surface, "#00BFFF", (self.x, self.y, self.w * ratio, self.h))

        #La clase de la rock con sus atributos y funciones
        class Rock(pygame.sprite.Sprite):
            def __init__(self, x, y):
                pygame.sprite.Sprite.__init__(self)
                self.image = pygame.image.load("img/Sprites/Coliders/rock.png")
                self.rect = self.image.get_rect()
                self.rect.topleft = [x,y]
                self.image = pygame.transform.rotate(self.image, -45)

            def update(self):
                #Se quedan en su lugar al morir
                if game_over == False:
                    self.rect.x -= 2

        #La clase de la rock con sus atributos y funciones
        class Bottle(pygame.sprite.Sprite):
            def __init__(self, x, y):
                pygame.sprite.Sprite.__init__(self)
                self.image = pygame.image.load("img/Sprites/Coliders/botella.png")
                self.rect = self.image.get_rect()
                self.rect.topleft = [x,y]

            def update(self):
                #Se quedan en su lugar al morir
                if game_over == False:
                    self.rect.x -= 2

        #La clase de la bolsa con sus atributos y funciones
        class FishTraped(pygame.sprite.Sprite):
            def __init__(self, x, y):
                pygame.sprite.Sprite.__init__(self)
                self.image = pygame.image.load("img/Sprites/FishAnimation/pez_atrapado.png")
                self.rect = self.image.get_rect()
                self.rect.topleft = [x,y]

            def update(self):
                if game_over == False:
                    self.rect.x -= 2

        #La clase de la bolsa con sus atributos y funciones
        class Bag(pygame.sprite.Sprite):
            def __init__(self, x, y):
                pygame.sprite.Sprite.__init__(self)
                self.image = pygame.image.load("img/Sprites/Coliders/bolsa.png")
                self.rect = self.image.get_rect()
                self.rect.topleft = [x,y]

            def update(self):
                if game_over == False:
                    self.rect.x -= 2

        #Definimos el boton para pasar al siguiente nivel
        def ButtonNextLevel():
            PLAY_MOUSE_POS = pygame.mouse.get_pos()

            NEXT = Button(image=(None), pos=(640, 400),
                                    text_input=Configuracion.get(langueje, {}).get("buttonNext"), font=get_font(50), base_color="White", hovering_color="Green")
            NEXT.changeColor(PLAY_MOUSE_POS)
            NEXT.update(PANTALLA)

            #Bucle para cerrar el juego
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                #Evento para detectar el mouse sobre el boton y funcion de este
                if event.type == pygame.MOUSEBUTTONDOWN:
                        if NEXT.checkForInput(PLAY_MOUSE_POS):
                            Level3()

        #Funcion para imprimir las teclas en pantalla
        def keys_on_screen():
            draw_text(Configuracion.get(langueje, {}).get("keysControl"), font2, black, 1040, 380)
            PANTALLA.blit(esc_key, (1030, 410))
            draw_text(Configuracion.get(langueje, {}).get("keysPaused"), font3, black, 1100, 446)
            PANTALLA.blit(r_key, (1030, 460))
            draw_text(Configuracion.get(langueje, {}).get("keysReset"), font3, black, 1100, 490)
            PANTALLA.blit(q_key, (1030, 505))
            draw_text(Configuracion.get(langueje, {}).get("keysExit"), font3, black, 1100, 535)
            PANTALLA.blit(flecha_up, (1020, 545))
            draw_text(Configuracion.get(langueje, {}).get("keysUpMusic"), font3, black, 1100, 577)
            PANTALLA.blit(flecha_down, (1010, 580))
            draw_text(Configuracion.get(langueje, {}).get("keysDownMusic"), font3, black, 1100, 620)

        #Se declaran los objetos como grupos
        submarine_group = pygame.sprite.Group()
        rock_group = pygame.sprite.Group()
        pez_group = pygame.sprite.Group()
        bag_group = pygame.sprite.Group()
        bottle_group = pygame.sprite.Group()

        #En la variable flappy almacenamos la ubicacion donde aparecera el buzo
        flappy = DelfinBuzo(100, int(H / 2))
        #Al grupo le agregamos la variable flappy
        submarine_group.add(flappy)

        #Asigna los valores a la clase vida
        fuel_bar = FuelBar(500, 35, 300, 40, 5000)
        fuel_bar.hp = 5000

        #Carga de imagenes de victoria
        images = []
        for i in range(1,5):
            name = "img/Sprites/VictoryAnimation/victory"+str(i)+".png"
            images.append(pygame.image.load(name))

        #Bucle principal del juego
        running = True
        while running:

            #Guardamos en una variable una funcion de tecla mantenida
            keys = pygame.key.get_pressed()

            #Movimiento en bucle del fondo del juego
            x_relativa = VelFondo % fondo.get_rect().width
            PANTALLA.blit(fondo,(x_relativa - fondo.get_rect().width,0))
            if x_relativa < W:
                PANTALLA.blit(fondo,(x_relativa,0))
            #Velocidad del fondo
            VelFondo -= 2
            #Velocidad del juego total
            clock.tick(fps)

            #Muestra todo en pantalla
            submarine_group.draw(PANTALLA)
            submarine_group.update()
            rock_group.draw(PANTALLA)
            rock_group.update()
            pez_group.draw(PANTALLA)
            pez_group.update()
            bag_group.draw(PANTALLA)
            bag_group.update()
            bottle_group.draw(PANTALLA)
            bottle_group.update()
            
            #Si la victoria todavia no esta hecha muestra el score, texto y controles
            if victory == False:
                #Muestra el score
                PANTALLA.blit(oxygen_ico, (450,15))
                draw_text(str(score), font, white, 1100, 20)
                draw_text(("/7"), font, white, 1130, 20) 
                PANTALLA.blit(fish_ico, (1190,25))

                draw_text(str(score2), font, white, 1100, 80)
                draw_text(("/5"), font, white, 1130, 80)
                PANTALLA.blit(bag_ico, (1200,80)) 
                fuel_bar.draw(PANTALLA)
                if langueje == "en":
                    draw_text(Configuracion.get(langueje, {}).get("oxigen"), font2, black, 575, 0)
                elif langueje == "es":
                    draw_text(Configuracion.get(langueje, {}).get("oxigen"), font2, black, 570, 0)
                

            
            #Cuando empizas el juego empieza muestra instrucciones
            if swimming == False and game_over == False:
                draw_text(Configuracion.get(langueje, {}).get("swimming"), font2, black, 400, 340)
                PANTALLA.blit(click1, (588, 315))
                #Funcion que muestre las teclas
                keys_on_screen()
            
            #Revisa que el submarino no se salga del agua
            if flappy.rect.top < 0:
                flappy.rect.top = 0
            
            #Revisa la colision del submarino con la roca
            if pygame.sprite.groupcollide(submarine_group, rock_group, False, False):
                game_over = True
            if pygame.sprite.groupcollide(submarine_group, bottle_group, False, False):
                game_over = True
    
            #Revisa la colision del submarino con el pez
            hitsfish = pygame.sprite.groupcollide(submarine_group, pez_group, False, True)

            hitsbag = pygame.sprite.groupcollide(submarine_group, bag_group, False, True)

            #bucle donde se van sumando los puntos por colisiones con el pescado
            for hit in hitsfish:
                if score < 7:
                    score += 1
                recolection.play()
            
            #bucle donde se van sumando los puntos por colisiones con la bolsa
            for hit in hitsbag:
                if score2 < 5:
                    score2 += 1
                recolection.play()

            #Defino la funcion de los controles de volumen
            def AudioControl():
                if keys[pygame.K_DOWN] and pygame.mixer_music.get_volume() > 0.0:
                    pygame.mixer.music.set_volume(pygame.mixer_music.get_volume() - 0.01)
                    PANTALLA.blit(sonido_abajo, (1150,25))
                elif keys[pygame.K_DOWN] and pygame.mixer_music.get_volume() == 0.0:
                    PANTALLA.blit(sonido_mute, (1150,25))

                #Sube volumen
                if keys[pygame.K_UP] and pygame.mixer_music.get_volume() < 1.0:
                    pygame.mixer.music.set_volume(pygame.mixer_music.get_volume() + 0.01)
                    PANTALLA.blit(sonido_arriba, (1150,25))
                elif keys[pygame.K_UP] and pygame.mixer_music.get_volume() == 1.0:
                    PANTALLA.blit(sonido_max, (1150,25))

            #Detecta si el jugador gana
            if score == 7 and score2 == 5 and game_over == False:
                victory = True
                def WinScreen():
                    #Se limpia todos los objetos
                    rock_group.empty()
                    pez_group.empty()
                    bag_group.empty()
                    submarine_group.empty()
                    bottle_group.empty()
                    #Muestra la imagen de victoria animada
                    frame = int(time.time()*10) % 4
                    PANTALLA.blit(images[frame], (0, 0))
                    #Muestra el boton de next
                    ButtonNextLevel()
                    #Se detiene la musica
                    pygame.mixer.music.stop()
                    for sound in hitsfish:
                        victory_sound.play()
                WinScreen()

            #Revisa que el submarino toque el suelo
            if flappy.rect.bottom >= 800:
                game_over = True
                swimming = False
                
                

            #Checa que el juego no llegue a Game Over
            if game_over == False and swimming == True:
                #Generador de roca
                time_now = pygame.time.get_ticks()
                if time_now - last_rock > frecuencia_rock:
                    rock_spawn = random.randint(100, 600)
                    rock = Rock(W, + rock_spawn)
                    rock_group.add(rock)
                    last_rock = time_now
            
            #Checa que el juego no llegue a Game Over
            if game_over == False and swimming == True:
                #Generador de botella
                time_now = pygame.time.get_ticks()
                if time_now - last_bottle > frecuencia_bottle:
                    bottle_spawn = random.randint(-100, 200)
                    bottle = Bottle(W, int(H / 2) + bottle_spawn)
                    bottle_group.add(bottle)
                    last_bottle = time_now

            #Checa que el juego no llegue a Game Over
            if game_over == False and swimming == True:
                #Generador de pescado
                time_now = pygame.time.get_ticks()
                if time_now - ultimo_pez > frecuencia_pez:
                    pez_spawn = random.randint(100, 600)
                    pez = FishTraped(W, + pez_spawn)
                    pez_group.add(pez)
                    ultimo_pez = time_now

            #Checa que el juego no llegue a Game Over
            if game_over == False and swimming == True:
                #Generador de bolsa
                time_now = pygame.time.get_ticks()
                if time_now - ultima_bag > frecuencia_bag:
                    bag_spawn = random.randint(200, 600)
                    bag = Bag(W, + bag_spawn)
                    bag_group.add(bag)
                    ultima_bag = time_now

            #Checa que el juego llegue a GameOver y dibuja los botones
            if game_over == True:
                pygame.mixer.music.stop()
                score = 0
                VelFondo = 0
                if langueje == "es":
                    draw_text(Configuracion.get(langueje, {}).get("overReset"), font2, black, W / 3.5, 330)
                    draw_text(Configuracion.get(langueje, {}).get("overExit"), font2, black, W / 3.1, 380)
                    draw_text(Configuracion.get(langueje, {}).get("teaching"), font2, red, 500, 250)
                    PANTALLA.blit(r_key, (490, 310))
                    PANTALLA.blit(q_key, (535, 360))
                if langueje == "en":
                    draw_text(Configuracion.get(langueje, {}).get("overReset"), font2, black, 450, 330)
                    draw_text(Configuracion.get(langueje, {}).get("overExit"), font2, black, 500, 380)
                    draw_text(Configuracion.get(langueje, {}).get("teaching"), font2, red, 550, 250)
                    PANTALLA.blit(r_key, (575, 310))
                    PANTALLA.blit(q_key, (625, 360))
                
            #Si el jugador muere reproduce el sonido
            if game_over == True and sound == True:
                death_sound.play()
                #La variable la vuelve falsa para que el if no se cumpla y no reproduzca en bucle
                sound = False

            #El decremento de la vida si el jugador empieza a jugar
            if swimming == True and game_over == False and victory == False:
                fuel_bar.hp -= 1
                if fuel_bar.hp <= 0:
                    game_over = True
                    death_sound.play()
                    
                        

            #Evento para poder cerrar la ventana del juego y no se quede en bucle infinito
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                    pygame.quit()
                    exit()
                #Detecta que el juego empiece al clickear
                if event.type == pygame.MOUSEBUTTONDOWN and swimming == False and game_over == False:
                    swimming = True
                #Detecta que el juego empiece al presionar space
                if event.type == pygame.KEYDOWN and swimming == False and game_over == False:
                    if event.key == pygame.K_SPACE:
                        swimming = True
                #Evento para detectar una pulsacion de tecla
                if event.type == pygame.KEYDOWN:
                    #Si la tecla presionada es Escape y el juego ya empezo
                    if event.key == pygame.K_ESCAPE and game_over == False and swimming == True:
                        if langueje == "es":
                            PANTALLA.blit(esc_key, (495, 345))
                        if langueje == "en":
                            PANTALLA.blit(esc_key, (530, 345))
                        keys_on_screen()
                        #Se va la funcion pause que es un bucle while
                        pause()
                    if event.key == pygame.K_r:
                        Level3()
                    if event.key == pygame.K_q:
                        pygame.mixer.music.stop()
                        #Carga el menu
                        from Menu import MenuTotal
                        MenuTotal()
                        
            #Carga el control de audio cuando carga el nivel            
            AudioControl()
            #Funcion para actualizar la pantalla constantemente
            pygame.display.update()