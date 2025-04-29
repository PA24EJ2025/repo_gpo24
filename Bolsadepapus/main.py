#1. Importar el framework o paquete
import pygame
import sys
#2. Definir constantes
ANCHO_VENTANA = 600
ALTO_VENTANA = 400
COLOR_FONDO = (30, 30, 30)
FPS = 60
#3. Inicializar pygame
pygame.init()

#4. Cargar recursos (imagenes)

imagen_perfil = pygame.image.load("Bolsadepapus/images.png")

#5. Inicializar variables
ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Mover Foto de Perfil")
reloj = pygame.time.Clock()

# Clase Perfil
class Perfil:
    def __init__(self, x, y, alto, ancho, velocidad):
        self.x = x
        self.y = y
        self.alto = alto
        self.ancho = ancho
        self.velocidad = velocidad
        self.imagen = pygame.transform.scale(imagen_perfil, (self.ancho, self.alto))

    def mostrar(self, ventana):
        ventana.blit(self.imagen, (self.x, self.y))

perfil = Perfil(x=100, y=100, alto=80, ancho=80, velocidad=5)

#6. Ciclo infinito
while True:
    # 7. Verificar y manejar los eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #7. Verificar y manejar los eventos
    #8. Realizar cualquier acción por frame

    #9. Limpiar la ventana

    #10. Dibujar elementos en la ventana
    
    #11. Actualizar la ventana
    
    #12. Ralentizar un poco las cosas