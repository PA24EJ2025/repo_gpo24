# Importar el framework o paquete
import pygame
import sys
from pygame.locals import *

# Definir constantes
ANCHO_VENTANA = 800
ALTO_VENTANA = 600
NEGRO = (0, 0, 0)

# Inicializar pygame
pygame.init()
pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("La ventana donde mueves una foto.exe")

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

perfil = Perfil(ANCHO_VENTANA // 2, ALTO_VENTANA // 2, 80, 80, 5)
perfil.cargar_imagen("foto_perfil.png")

#5. Inicializar variables
reloj = pygame.time.Clock()

#6. Ciclo infinito
while True:

    #7. Verificar y manejar los eventos
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()

    #8. Realizar cualquier acción por frame
    teclas = pygame.key.get_pressed()
    if teclas[K_UP] and perfil.y > 0:
        perfil.y -= perfil.velocidad
    if teclas[K_DOWN] and perfil.y < ALTO_VENTANA - perfil.alto:
        perfil.y += perfil.velocidad
    if teclas[K_LEFT] and perfil.x > 0:
        perfil.x -= perfil.velocidad
    if teclas[K_RIGHT] and perfil.x < ANCHO_VENTANA - perfil.ancho:
        perfil.x += perfil.velocidad

    #9. Limpiar la ventana
    pantalla.fill(NEGRO)

    #10. Dibujar elementos en la ventana
    perfil.mostrar(pantalla)
    
    #11. Actualizar la ventana
    pygame.display.update()
    
    #12. Ralentizar un poco las cosas
    reloj.tick(60)