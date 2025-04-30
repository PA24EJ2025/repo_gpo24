class Perfil:
    def __init__(self,x,y,alto,ancho,velocidad):
        self.x = x
        self.y = y
        self.alto = alto
        self.ancho = ancho
        self.velocidad = velocidad
        self.imagen = pygame.image.load('GallardoGallagaky/canales.png')
        self.imagen_nueva = pygame.transform.scale(self.imagen,(80,80))

    def mostrar(self,ventana):
        ventana.blit(self.imagen_nueva,(self.x, self.y))

import pygame
import sys
from pygame.locals import *

pygame.init()

#Pantalla
ANCHO = 800
ALTO = 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
x= 0
y=0
velocidad = 60
reloj = pygame.time.Clock()
foto = Perfil(x, y, ANCHO, ALTO, velocidad)


#Ciclo infinito 
while True:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
    
        elif evento.type ==pygame.KEYDOWN:   
                if evento.key == K_UP:
                    foto.y -= foto.velocidad
                if evento.key == K_DOWN:
                    foto.y += foto.velocidad
                if evento.key == K_LEFT:
                    foto.x -= foto.velocidad
                if evento.key == K_RIGHT:
                    foto.x += foto.velocidad

    ventana.fill((255, 255, 255))
    foto.mostrar(ventana)
    pygame.display.flip()
    reloj.tick(velocidad)
