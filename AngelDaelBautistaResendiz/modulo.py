import pygame
from pygame.locals import *

class Perfil:
    def __init__(self, x, y, velocidad):
        self.x = x
        self.y = y
        self.ancho = 80
        self.alto = 80
        self.imagen = pygame.image.load("fotoperfil.png")
        self.velocidad = velocidad
    
    def dibujar(self, ventana):
        ventana.blit(self.imagen, (self.x, self.y))