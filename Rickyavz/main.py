#1. Importar el framework o paquete
import pygame
from pygame.locals import *
import sys
import random
 

ANCHO=640
ALTO=480
FPS=30
BLANCO=(255,255,255)
SIZE_CUADRO=10
ANCHO_MAX = ANCHO - SIZE_CUADRO
ALTO_MAX = ALTO- SIZE_CUADRO
pygame.init()
ventana = pygame.display.set_mode((ANCHO, ALTO))
reloj = pygame.time.Clock() 

#4. Cargar recursos (imagenes)
#5. Inicializar variables
#6. Ciclo infinito
ventana.fill(BLANCO) 
while True:

    #7. Verificar y manejar los eventos
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit() 