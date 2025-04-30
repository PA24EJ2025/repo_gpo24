# Importar el framework o paquete
import pygame

# Definir constantes
ANCHO_VENTANA = 800
ALTO_VENTANA = 600
NEGRO = (0, 0, 0)

# Inicializar pygame
pygame.init()
pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Mover la foto de perfil")

# Cargar recursos (imagenes)
class Perfil:
    def __init__(self, x, y, alto, ancho, velocidad):
        self.x = x
        self.y = y
        self.alto = alto
        self.ancho = ancho
        self.velocidad = velocidad
        self.imagen = None

    def cargar_imagen(self, ruta):
        self.imagen = pygame.image.load(ruta)
        self.imagen = pygame.transform.scale(self.imagen, (self.ancho, self.alto))

    def mostrar(self, ventana):
        if self.imagen:
            ventana.blit(self.imagen, (self.x, self.y))