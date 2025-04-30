import pygame

class Perfil:
    def __init__ (self,x,y,ancho,alto,velocidad):
         self.x = x
         self.y = y
         self.ancho = ancho
         self.alto =alto
         self.imagen = pygame.image.load("perfil.png")
         self.velocidad = velocidad
         
