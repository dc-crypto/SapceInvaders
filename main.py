import pygame
import random
import math

# inicializa pygame
pygame.init()

# crea pantalla
pantalla = pygame.display.set_mode((800, 600))

# Titulo e icono
pygame.display.set_caption("Invasión Espacial")
icono = pygame.image.load("ovni.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load("fondo.jpg")

# variables del Jugador
img_jugador = pygame.image.load("rocket.png")
jugador_x = 368
jugador_y = 500
jugador_x_cambio = 0

# variables del enemigo
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_de_enemigos=8

for e in range(cantidad_de_enemigos):
    img_enemigo.append(pygame.image.load("nave-espacial.png"))
    enemigo_x.append(random.randint(0, 736))
    enemigo_y.append(random.randint(50, 200))
    enemigo_x_cambio.append(0.3)
    enemigo_y_cambio.append(50)

# variables de la bala
img_bala = pygame.image.load("bala.png")
bala_x = 0
bala_y = 500
bala_x_cambio = 0
bala_y_cambio = 0.3
bala_visible = False

#puntaje
puntaje=0
fuente=pygame.font.Font("Invaders.ttf",32)
texto_x=10
texto_y=10

#funcion mostrar puntaje
def mostrar_puntaje(x,y):
    texto=fuente.render(f"Puntaje :{puntaje}", True, (255,255,255))
    pantalla.blit(texto,(x,y))



# funcion jugador
def jugador(jugador_x, jugador_y):
    pantalla.blit(img_jugador, (jugador_x, jugador_y))


# funcion enemigo
def enemigo(x, y, ene):
    pantalla.blit(img_enemigo[ene], (x, y))


# disparar bala

def disparar_bala(x, y):
    global bala_visible  # para poder llamar a la bala se define global
    bala_visible = True
    pantalla.blit(img_bala, (x + 16, y + 10))


# funcion detectar colisiones
def hay_colision(x_1, y_1, x_2, y_2):
    distancia = math.sqrt(math.pow(x_2 - x_1, 2) + math.pow(y_2 - y_1, 2))
    if distancia < 27:
        return True
    else:
        False


# Loop del juego
se_ejecuta = True
while se_ejecuta:

    # cargar imagen de fondo
    pantalla.blit(fondo, (0, 0))

    # evento cerrar
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        # evento presionar tecla
        if evento.type == (pygame.KEYDOWN):
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -0.3
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = +0.3
            if evento.key == pygame.K_SPACE:
                if not bala_visible:
                    bala_x = jugador_x
                    disparar_bala(bala_x, jugador_y)

        # soltar flecha
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0

    # Modificar ubicación del jugador
    jugador_x += jugador_x_cambio

    # mantener entre los bordes al jugador
    if jugador_x <= 0:
        jugador_x = 0
    if jugador_x >= 736:
        jugador_x = 736

    # Modificar ubicación del enemigo
    for e in range(cantidad_de_enemigos):
        enemigo_x[e] += enemigo_x_cambio[e]

        # mantener entre los bordes al enemigo
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = 0.2
            enemigo_y[e] += enemigo_y_cambio[e]
        if enemigo_x[e] >= 736:
            enemigo_x_cambio[e] = -0.2
            enemigo_y[e] += enemigo_y_cambio[e]

        # colision
        colision = hay_colision(enemigo_x[e], enemigo_y[e], bala_x, bala_y)
        if colision:
            bala_y = 500
            bala_visible = False
            puntaje += 1
            enemigo_x[e] = random.randint(0, 736)
            enemigo_y[e] = random.randint(50, 200)

        enemigo(enemigo_x[e], enemigo_y[e],e)

    # movimiento bala
    if bala_y <= 64:
        bala_y = 500
        bala_visible = False
    if bala_visible:
        disparar_bala(bala_x, bala_y)
        bala_y -= bala_y_cambio



    jugador(jugador_x, jugador_y)

    #mostrar puntaje
    mostrar_puntaje(texto_x,texto_y)
    # Actualizar pantalla
    pygame.display.update()
