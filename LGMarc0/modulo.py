import pygame 

pygame.init()

WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Movimiento Perfil")

class Perfil:
    def __init__(self, x, y, velocidad):
        self.ancho = 80
        self.alto = 80
        self.x = x
        self.y = y
        self.velocidad_x = -velocidad
        self.velocidad_y = velocidad
        self.imagen = pygame.image.load("modulo.png")  # Asegúrate de tener "foto.png" en el mismo directorio
        self.imagen = pygame.transform.scale(self.imagen, (self.ancho, self.alto))