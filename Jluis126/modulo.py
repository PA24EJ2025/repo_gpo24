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
pygame.display.set_caption("foto de perfil movida")

# 4. Cargar recursos (imagenes)
imagen_original = pygame.image.load('gatito pretencioso')
imagen_modificada = pygame.transform.scale(imagen_original, (ANCHO, ALTO))

# 5. Inicializar variables
reloj = pygame.time.Clock()
running = True

# 6. Ciclo infinito
while running:
    # 7. Verificar y manejar los eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 8. Realizar cualquier acción por frame
    # (En este caso no hay acciones aparte de dibujar)

    # 9. Limpiar la ventana
    ventana.fill((0, 0, 0, 0))  # Fondo negro con transparencia

    # 10. Dibujar elementos en la ventana
    ventana.blit(imagen_modificada, (X//2 - ANCHO//2, Y//2 - ALTO//2))

    # 11. Actualizar la ventana
    pygame.display.update()

    # 12. Ralentizar un poco las cosas
    reloj.tick(60)

# Salir de pygame
pygame.quit()
sys.exit()