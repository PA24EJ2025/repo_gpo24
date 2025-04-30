class Perfil:
    def _init_(self,x,y,alto,ancho,velocidad):
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

pygame.init()

#Pantalla
ancho = 600
alto = 500
ventana = pygame.display.set_mode((ancho, alto))
x= 0
y=0
velocidad = 60
reloj = pygame.time.Clock()

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()