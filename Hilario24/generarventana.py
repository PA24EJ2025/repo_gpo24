import pygame
from pygame.locals import *
import sys
from icono import pinguino 


ANCHO_VENTANA = 1000
ALTO_VENTANA = 780
FPS =30
BLANCO =(255,255,255)

pygame.init()
ventana = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.display.set_caption ("moverimagendeperfil")
reloj = pygame.time.Clock()


icono = pinguino("pinguino", 5, 0, 80, 80, 5)
while True:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()   

    teclas= pygame.key.get_pressed() 
    if teclas[K_LEFT]:
        icono.x -= icono.velocidad
    if teclas[K_RIGHT]:
        icono.x += icono.velocidad
    if teclas[K_UP]:
        icono.y -= icono.velocidad
    if teclas[K_DOWN]:
        icono.y += icono.velocidad
    ventana.fill(BLANCO)   
    icono.dibujar(ventana)

    pygame.display.update()
    reloj.tick(FPS)
