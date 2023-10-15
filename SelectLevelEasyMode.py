import pygame, sys
from JSON import Load
import Menu as cfg

def SelectorEasy():
    pygame.init()

    #Carga de idioma
    Configuracion,langueje = Load()
    langueje = cfg.idioma_actual

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
        mouse_x, mouse_y = pygame.mouse.get_pos()

    #(PENDIENTE)Animacion del pez
        if BacknewLevel1.collidepoint(mouse_x, mouse_y):
                draw_text("hola", font2,"white",100,100)
                
        if BacknewLevel2.collidepoint(mouse_x, mouse_y):
                draw_text("hola", font2,"white",100,100)

        if BacknewLevel3.collidepoint(mouse_x, mouse_y):
                draw_text("hola", font2,"white",100,100)

    #Salir
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    #(PENDIENTE)Entrar al nivel
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if BacknewLevel1.collidepoint(mouse_x, mouse_y):
                        pygame.mixer_music.stop()
                        from GameEasy import start_menu
                        from GameEasy import Level1
                        start_menu()
                        Level1()



        pygame.display.update()