import pygame

class pinguino:
    def __init__(self,nombre,x,y,ancho,alto,velocidad):
        self.velocidad = velocidad
        self.x = x
        self.y =y
        self.ancho = ancho
        self.alto = alto
        self.imagen = pygame.image.load("pinguino.png") 
        self.imagen = pygame.transform.scale(self.imagen, (self.ancho, self.alto))
     

    
    def dibujar(self,ventana):
        ventana.blit(self.imagen,(self.x, self.y))
        