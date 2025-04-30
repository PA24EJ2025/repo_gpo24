class Perfil:
    def __init__(self,x,y,ancho_i,alto_i,imagen,velocidad):
        self.x=x
        self.y=y
        self.ancho_1=ancho_i
        self.alto_i=alto_i
        self.imagen= pygame.image.load("kratos.jpg")
        self.imagen=pygame.transform.scale(self.imagen,(ancho_i,alto_i))
        self.velocidad=velocidad
    def mover(self,dx,dy):
        self.x += dx + self.velocidad
        self.y += dy + self.velocidad
        self.x = max(0, min(self.x, ANCHO - self.ancho_i))
        self.y = max(0, min(self.y, ALTO - self.alto_i))
    def dibujar(self,superficie):
        superficie.blit(self.imagen,(self.x,self.y))

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
    teclas=pygame.key.get_pressed()
    dx,dy=0,0
    if teclas[K_LEFT]:
        dx=-1
    if teclas[K_RIGHT]:
        dx=-1
    if teclas[K_UP]:
        dy=-1
    if teclas[K_DOWN]:
        dy=1
    