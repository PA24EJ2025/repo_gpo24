import pygame
def __init__(self,nombre,x,y,ancho,alto):
        self.nombre = nombre
        self.x = x
        self.y = y 
        self.ancho = ancho
        self.alto = alto 
        self.imagen = pygame.image.load ("imagen_perfil.png")
        def dibujar(self,ventana):
        ventana.blit(self.imagen,
                     (self.x,self.y,
                      self.ancho,self.alto))