import pygame
from pygame.locals import *
import sys
import perfil

ANCHO_VENTANA=600
ALTO_VENTANA=600
FPS=30
SIZE_CUADRO=80
ANCHO_MAX=ANCHO_VENTANA - SIZE_CUADRO
ALTO_MAX=ALTO_VENTANA - SIZE_CUADRO

pygame.init()
ventana = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
reloj = pygame.time.Clock()

while True:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
            
    obj_perfil = perfil.Foto("Bryan",10,10,90,90)
    obj_perfil.dibujar(ventana)
    
    
    #obj_perfil.mover(ventana)
    
    pygame.display.update()
    reloj.tick(FPS)