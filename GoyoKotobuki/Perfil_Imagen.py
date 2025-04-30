#1. Importar el framework o paquete
import pygame
import sys

#2. Definir constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
FPS = 60

#3. Inicializar pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mover Imagen de Perfil")

#4. Cargar recursos (imagenes)
original_image = pygame.image.load("TsumugiKotobuki.jpg")  # Cambia esto por tu archivo
pygame.image.save(original_image, "TsumugiKotobuki.jpg")  # Guardar como PNG
image = pygame.image.load("TsumugiKotobuki.jpg")  # Cargar PNG

#5. Inicializar variables
image_rect = image.get_rect()
image_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
clock = pygame.time.Clock()

#6. Ciclo infinito
running = True
while running:
    #7. Verificar y manejar los eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #8. Realizar cualquier acción por frame
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        image_rect.x -= 5
    if keys[pygame.K_RIGHT]:
        image_rect.x += 5
    if keys[pygame.K_UP]:
        image_rect.y -= 5
    if keys[pygame.K_DOWN]:
        image_rect.y += 5

    #9. Limpiar la ventana
    screen.fill(WHITE)

    #10. Dibujar elementos en la ventana
    screen.blit(image, image_rect)

    #11. Actualizar la ventana
    pygame.display.flip()

    #12. Ralentizar un poco las cosas
    clock.tick(FPS)

# Salir de Pygame
pygame.quit()
sys.exit()