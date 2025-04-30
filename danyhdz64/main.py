class Perfil:
    def __init__(self, x, y, ancho, alto, imagen, velocidad):
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = alto
        self.imagen = imagen
        self.velocidad = velocidad
#1. Importar el framework o paquete
import pygame
from pygame.locals import *
import sys
import random
#2. Definir constantes
ANCHO_VENTANA = 1900
ALTO_VENTANA = 1000
FPS = 30
BLANCO_CUADRO = 10
ANCHO_MAX = ANCHO_VENTANA- SIZE_CUADRO
ALTO_MAX = ALTO_VENTANA- SIZE_CUDARO
#3. Inicializar pygame
pygame.init()
ventana = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
reloj = pygame.time.Clock()
#4. Cargar recursos (imagenes)

#5. Inicializar variables

#6. Ciclo infinito
ventana.fill(BLANCO)
while True:
#7. Verificar y manejar los eventos
    for evento in pygame.event.get():
        if evento.type ==QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type ==KEYDOWN:
            if evento.key == K_n:
                pos_x = random.randrange(ANCHO_MAX)
                pos_y = random.randrange(ALTO_MAX)
   
#8. Realizar cualquier acción por frame
    
#9. Limpiar la ventana

#10. Dibujar elementos en la ventana
    
#11. Actualizar la ventana
    pygame.display.update()
#12. Ralentizar un poco las cosas
    reloj.tick(FPS)