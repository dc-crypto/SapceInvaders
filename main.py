import pygame
import random
#inicializa pygame
pygame.init()

#crea pantalla
pantalla = pygame.display.set_mode((800,600))

#Titulo e icono
pygame.display.set_caption("Invasión Espacial")
icono = pygame.image.load("ovni.png")
pygame.display.set_icon(icono)

#Jugador
img_jugador=pygame.image.load("rocket.png")
jugador_x=368
jugador_y=536
jugador_x_cambio=0

#enemigo
img_enemigo=pygame.image.load("nave-espacial.png")
enemigo_x=random.randint(0,736)
enemigo_y=random.randint(50,200)
enemigo_x_cambio=0.3
enemigo_y_cambio=50


#funcion jugador
def jugador(jugador_x,jugador_y):
    pantalla.blit(img_jugador,(jugador_x,jugador_y))

#funcion enemigo
def enemigo(enemigo_x,enemigo_y):
    pantalla.blit(img_enemigo,(enemigo_x,enemigo_y))

#Loop del juego
se_ejecuta=True
while se_ejecuta:
    pantalla.fill((205, 144, 228))

    #evento cerrar
    for evento in pygame.event.get():
        if evento.type==pygame.QUIT:
            se_ejecuta=False

        #presionar flecha
        if evento.type==(pygame.KEYDOWN):
            if evento.key==pygame.K_LEFT:
                jugador_x_cambio=-0.3
            if evento.key==pygame.K_RIGHT:
                jugador_x_cambio=+0.3

        #soltar flecha
        if evento.type==pygame.KEYUP:
            if evento.key==pygame.K_LEFT or evento.key==pygame.K_RIGHT:
                jugador_x_cambio = 0

    # Modificar ubicación del jugador
    jugador_x += jugador_x_cambio

    #mantener entre los bordes al jugador
    if jugador_x <=0:
        jugador_x=0
    if jugador_x >=736:
        jugador_x=736


    # Modificar ubicación del enemigo
    enemigo_x += enemigo_x_cambio

    # mantener entre los bordes al enemigo
    if enemigo_x <= 0:
        enemigo_x_cambio = 0.3
    if enemigo_x >= 736:
        enemigo_x_cambio = -0.3



    jugador(jugador_x,jugador_y)
    enemigo(enemigo_x,enemigo_y)

    #Actualizar pantalla
    pygame.display.update()




