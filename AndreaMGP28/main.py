#1. Importar el framework o paquete
import pygame
import sys
from pygame.locals import *

#2. Definir constantes
ROSA = (221, 160, 160)
ANCHO_VENTANA = 640
ALTO_VENTANA = 480
FPS = 30

#3. Inicializar pygame
pygame.init()
ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Mover foto con teclas")
reloj = pygame.time.Clock()

#4. Cargar recursos (imágenes)
foto = pygame.image.load("AndreaMGP28/gatosuavitel.png")

#5. Inicializar variables
class Perfil:
    def __init__(self, x, y, alto, ancho, velocidad):
        self.x = x
        self.y = y
        self.alto = alto
        self.ancho = ancho
        self.velocidad = velocidad
        self.foto = pygame.transform.scale(foto, (ancho, alto))

    def mostrar(self, ventana):
        ventana.blit(self.foto, (self.x, self.y))

perfil = Perfil(x=100, y=100, alto=80, ancho=80, velocidad=5)

#6. Ciclo infinito
while True:
    #7. Verificar y manejar los eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #8. Realizar cualquier acción por frame
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        perfil.x -= perfil.velocidad
    if teclas[pygame.K_RIGHT]:
        perfil.x += perfil.velocidad
    if teclas[pygame.K_UP]:
        perfil.y -= perfil.velocidad
    if teclas[pygame.K_DOWN]:
        perfil.y += perfil.velocidad

    #9. Limpiar la ventana
    ventana.fill(ROSA)

    #10. Dibujar elementos en la ventana
    perfil.mostrar(ventana)

    #11. Actualizar la ventana
    pygame.display.update()

    #12. Ralentizar un poco las cosas
    reloj.tick(FPS)
