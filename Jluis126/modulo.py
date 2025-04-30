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
imagen_original = pygame.image.load('Jluis126\gatito pretencioso.png')
imagen_modificada = pygame.transform.scale(imagen_original, (ANCHO, ALTO))

# 5. Inicializar variables
x_pos = X // 2 - ANCHO // 2  # Posición inicial de la imagen (centrada)
y_pos = Y // 2 - ALTO // 2
reloj = pygame.time.Clock()
running = True

# 6. Ciclo infinito
while running:
    # 7. Verificar y manejar los eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 8. Detectar las teclas presionadas para mover la imagen
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:  # Flecha izquierda
        x_pos -= 5
    if keys[pygame.K_RIGHT]:  # Flecha derecha
        x_pos += 5
    if keys[pygame.K_UP]:  # Flecha arriba
        y_pos -= 5
    if keys[pygame.K_DOWN]:  # Flecha abajo
        y_pos += 5

    # 9. Limpiar la ventana
    ventana.fill((0, 0, 0))  # Fondo negro (sin transparencia)

    # 10. Dibujar elementos en la ventana
    ventana.blit(imagen_modificada, (x_pos, y_pos))

    # 11. Actualizar la ventana
    pygame.display.update()

    # 12. Ralentizar un poco las cosas
    reloj.tick(60)

# Salir de pygame
pygame.quit()
sys.exit()
