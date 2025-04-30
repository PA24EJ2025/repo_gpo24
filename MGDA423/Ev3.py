#1. Importar el framework o paquete
import pygame
import sys
from pygame.locals import *

#2. Definir constantes
ANCHO_VENTANA = 645
ALTO_VENTANA = 480
AZUL_CLARO = (173, 216, 230)
CUADROS_POR_SEGUNDO = 30

#3. Inicializar pygame
pygame.init()
ventana = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.display.set_caption("Mover mi foto")
reloj = pygame.time.Clock()

#4. Cargar recursos (imagenes)
foto = pygame.image.load("MGDA423/gojo.gato.jpg")

#5. Inicializar variables y la clase Perfil
class Perfil:
    def __init__(self, x, y, alto, ancho, imagen, velocidad):
        self.x = x
        self.y = y
        self.alto = alto
        self.ancho = ancho
        self.imagen_original = imagen
        self.imagen = pygame.transform.scale(self.imagen_original, (ancho, alto))
        self.velocidad = velocidad

    def mostrar(self, ventana):
        ventana.blit(self.imagen, (self.x, self.y))

ancho_deseado = 160
alto_deseado = 160
velocidad_movimiento = 5
posicion_inicial_x = 80
posicion_inicial_y = 80

perfil = Perfil(posicion_inicial_x, posicion_inicial_y, alto_deseado, ancho_deseado, foto, velocidad_movimiento)

#6. ciclo infinito..
while True:
    #7. Verificar y manejar los eventos
    for evento in pygame.event.get():
        if evento.type == QUIT:
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
    ventana.fill(AZUL_CLARO)

    #10. Dibujar elementos en la ventana
    perfil.mostrar(ventana)

    #11... Actualizar la ventana
    pygame.display.update()

    #12. Ralentizar un poco las cosas
    reloj.tick(CUADROS_POR_SEGUNDO)