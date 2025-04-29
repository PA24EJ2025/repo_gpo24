# 1. Importar el framework o paquete
import pygame
import sys

# 2. Definir constantes
X = 500
Y = 500
ANCHO = 80
ALTO = 80

# 3. Inicializar pygame
pygame.init()

# Crear ventana
ventana = pygame.display.set_mode((X, Y))
pygame.display.set_caption("foto de perfil movida tocada o impune")

# 4. Cargar recursos (imagenes)
imagen_original = pygame.image.load('gatito pretencioso')
imagen_modificada = pygame.transform.scale(imagen_original, (ANCHO, ALTO))

# 5. Inicializar variables
reloj = pygame.time.Clock()
running = True

#6. Ciclo infinito
    #7. Verificar y manejar los eventos
    #8. Realizar cualquier acción por frame

    #9. Limpiar la ventana

    #10. Dibujar elementos en la ventana
    
    #11. Actualizar la ventana
    
    #12. Ralentizar un poco las cosas