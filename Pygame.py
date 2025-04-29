# 1. Importar el framework o paquete
import pygame
import sys

# 2. Inicializar pygame
pygame.init()

# 3. Definir constantes
ANCHO, ALTO = 1000, 1000
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
COLOR_FONDO = (255, 255, 255)  # Blanco

# 4. Definir la clase Perfil
class Perfil:
    def __init__(self, x, y, alto, ancho, ruta_imagen, velocidad):
        self.imagen = pygame.image.load(ruta_imagen)
        self.imagen = pygame.transform.scale(self.imagen, (ancho, alto))
        self.rect = self.imagen.get_rect()
        self.rect.topleft = (x, y)
        self.velocidad = velocidad

    def mover(self, teclas):
        if teclas[pygame.K_UP]:
            self.rect.y -= self.velocidad
        if teclas[pygame.K_DOWN]:
            self.rect.y += self.velocidad
        if teclas[pygame.K_LEFT]:
            self.rect.x -= self.velocidad
        if teclas[pygame.K_RIGHT]:
            self.rect.x += self.velocidad

    def dibujar(self, ventana):
        ventana.blit(self.imagen, self.rect)

# 5. Crear el objeto Perfil
foto_perfil = Perfil(100, 100, 80, 80, 'ElEmilio824/Minecraft.png', 5)

# 6. Ciclo principal
while True:
    # 7. Manejar eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 8. Movimiento del perfil
    teclas = pygame.key.get_pressed()
    foto_perfil.mover(teclas)

    # 9. Limpiar la ventana
    VENTANA.fill(COLOR_FONDO)

    # 10. Dibujar perfil
    foto_perfil.dibujar(VENTANA)

    # 11. Actualizar la ventana
    pygame.display.update()

    # 12. Ralentizar
    pygame.time.Clock().tick(60)

