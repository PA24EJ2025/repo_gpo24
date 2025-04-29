import pygame
from pygame.locals import *
import sys
import os

# Clase Perfil
class Perfil:
    def __init__(self, x, y, ancho, alto, imagen_path, velocidad):
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = alto
        self.imagen_original = pygame.image.load(imagen_path).convert_alpha()  # Cargar imagen
        self.imagen = pygame.transform.scale(self.imagen_original, (ancho, alto))  # Ajustar tamaño
        self.velocidad = velocidad

    def mover(self, dx, dy, ancho_ventana, alto_ventana):
        nuevo_x = self.x + dx * self.velocidad
        nuevo_y = self.y + dy * self.velocidad

        # Cambiar tamaño según dirección
        if dx > 0 or dy > 0:
            nuevo_ancho = self.ancho + 2
            nuevo_alto = self.alto + 2
        elif dx < 0 or dy < 0:
            nuevo_ancho = max(10, self.ancho - 2)
            nuevo_alto = max(10, self.alto - 2)
        else:
            nuevo_ancho = self.ancho
            nuevo_alto = self.alto

        # Verificar que no se salga de los límites
        if 0 <= nuevo_x <= ancho_ventana - nuevo_ancho and 0 <= nuevo_y <= alto_ventana - nuevo_alto:
            self.x = nuevo_x
            self.y = nuevo_y
            self.ancho = nuevo_ancho
            self.alto = nuevo_alto
            self.imagen = pygame.transform.scale(self.imagen_original, (self.ancho, self.alto))

    def dibujar(self, ventana):
        ventana.blit(self.imagen, (self.x, self.y))

# 1. Importar el framework o paquete
pygame.init()

# 2. Definir constantes
ANCHO_VENTANA = 800
ALTO_VENTANA = 600
FPS = 30
BLANCO = (255, 255, 255)

# 3. Inicializar pygame
ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Mover Imagen con Teclas")
reloj = pygame.time.Clock()

# 4. Cargar recursos (imagenes)
ruta_imagen = os.path.join(os.path.dirname(__file__), 'fotogithub.png')


# 5. Inicializar variables
x_inicial = (ANCHO_VENTANA // 2) - (80 // 2)  # Centrar en el medio
y_inicial = (ALTO_VENTANA // 2) - (80 // 2)
personaje = Perfil(x_inicial, y_inicial, 80, 80, ruta_imagen, velocidad=5)

# 6. Ciclo infinito
while True:
    # 7. Verificar y manejar los eventos
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()

    # 8. Realizar cualquier acción por frame
    teclas = pygame.key.get_pressed()
    if teclas[K_RIGHT]:
        personaje.mover(1, 0, ANCHO_VENTANA, ALTO_VENTANA)
    if teclas[K_LEFT]:
        personaje.mover(-1, 0, ANCHO_VENTANA, ALTO_VENTANA)
    if teclas[K_UP]:
        personaje.mover(0, -1, ANCHO_VENTANA, ALTO_VENTANA)
    if teclas[K_DOWN]:
        personaje.mover(0, 1, ANCHO_VENTANA, ALTO_VENTANA)

    # 9. Limpiar la ventana
    ventana.fill(BLANCO)

    # 10. Dibujar elementos en la ventana
    personaje.dibujar(ventana)

    # 11. Actualizar la ventana
    pygame.display.update()

    # 12. Ralentizar un poco las cosas
    reloj.tick(FPS)
