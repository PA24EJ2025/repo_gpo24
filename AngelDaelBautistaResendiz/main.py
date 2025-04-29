import pygame
import sys
from pygame.locals import *
from modulo import Perfil

BLANCO = (255, 255, 255)
ANCHO_VENTANA = 640
ALTO_VENTANA = 480
FPS = 75

pygame.init()
ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))

personaje = Perfil(ANCHO_VENTANA//2, ALTO_VENTANA//2, 5)

reloj = pygame.time.Clock()

while True:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
    
    teclas = pygame.key.get_pressed()
    
    if teclas[K_LEFT]:
        personaje.x -= 5
    if teclas[K_RIGHT]:
        personaje.x += 5
    if teclas[K_UP]:
        personaje.y -= 5
    if teclas[K_DOWN]:
        personaje.y += 5

    personaje.x = max(0, min(personaje.x, ANCHO_VENTANA - personaje.ancho))
    personaje.y = max(0, min(personaje.y, ALTO_VENTANA - personaje.alto))

    ventana.fill(BLANCO)
    personaje.dibujar(ventana)
    pygame.display.update()
    reloj.tick(FPS) 