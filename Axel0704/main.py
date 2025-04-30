import pygame
from pygame.locals import *
import sys

x = 0
y = 0
ancho = 500
alto = 300
ANC_VENTANA = 800
ALT_VENTANA = 700
FPS = 30
VELOCIDAD = 30

pygame.init()
ventana = pygame.display.set_mode((ANC_VENTANA, ALT_VENTANA))
reloj = pygame.time.Clock()

class Perfil:
    def __init__(self, x, y, ancho, alto, velocidad):
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = alto
        self.velocidad = velocidad
        
        self.img = pygame.image.load('C:/Users/Drawing x/Documents/repo_gpo24/Axel0704/foto.jpg')
        
        self.N_IMG = pygame.transform.scale(self.img, (80, 80))
        
    def Ver_imagen(self, ventana):
        ventana.blit(self.N_IMG, (self.x, self.y))

imagen = Perfil(x, y, ancho, alto, VELOCIDAD)

while True:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == KEYDOWN:
            if evento.key == K_UP:
                imagen.y -= imagen.velocidad
            if evento.key == K_DOWN:
                imagen.y += imagen.velocidad
            if evento.key == K_LEFT:
                imagen.x -= imagen.velocidad
            if evento.key == K_RIGHT:
                imagen.x += imagen.velocidad

   
    imagen.x = max(0, min(imagen.x, ANC_VENTANA - 80))
    imagen.y = max(0, min(imagen.y, ALT_VENTANA - 80))

    ventana.fill((0, 0, 0))
    imagen.Ver_imagen(ventana)
    pygame.display.flip()
    reloj.tick(FPS)
