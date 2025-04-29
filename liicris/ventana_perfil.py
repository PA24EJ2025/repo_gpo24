import pygame
from pygame.locals import *
import sys
from imagen_perfil import perfil

ANCHO_VENTANA = 400
ALTO_VENTANA = 360
FPS = 30
BLANCO = (255, 255, 255)

pygame.init()

ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Mover imagen de perfil")

reloj = pygame.time.Clock()

# Solo se crea una vez el objeto Perfil
imagenperfil = perfil(0, 0, 80, 80, 5)

while True:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()

    # Mover con las teclas
    teclas = pygame.key.get_pressed()
    if teclas[K_LEFT]:
        imagenperfil.x -= imagenperfil.velocidad
    if teclas[K_RIGHT]:
        imagenperfil.x += imagenperfil.velocidad
    if teclas[K_UP]:
        imagenperfil.y -= imagenperfil.velocidad
    if teclas[K_DOWN]:
        imagenperfil.y += imagenperfil.velocidad

    ventana.fill(BLANCO)
    imagenperfil.dibujar(ventana)
    pygame.display.update()
    reloj.tick(FPS)
