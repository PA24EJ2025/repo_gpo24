#1. Importar el framework o paquete
import pygame
from pygame.locals import *
import sys
                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
#2. Definir constantes
ANCHO_VENTANA = 700
ALTO_VENTANA = 480
TRANSPARENTE =(0, 0, 0)
FPS = 30
#3. Inicializar pygame
pygame.init()
#4. Cargar recursos (imagenes)
Foto_perfil = pygame.image.load("spidercat.png")
#5. Inicializar variables
ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Movimiento de foto")
reloj = pygame.time.Clock()
class Perfil:
    def __init__(self, x, y, alto, ancho, velocidad):
        self.x = x
        self.y = y
        self.alto = alto
        self.ancho = ancho
        self.velocidad = velocidad
        self.imagen = pygame.transform.scale(Foto_perfil, (self.ancho, self.alto))

    def mostrar(self, ventana):
        ventana.blit(self.imgen, (self.x, self.y))

Configuracion = Perfil(x=100, y=100, alto=90, ancho=90, velocidad=10)
#6. Ciclo infinito
ventana.fill(TRANSPARENTE)
while True:
    #7. Verificar y manejar los eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #8. Realizar cualquier acción por frame
    Movimiento = pygame.key.get_pressed()

    if Movimiento[pygame.K_LEFT]:
        Configuracion.x -= Configuracion.velocidad
        
    if Movimiento[pygame.K_RIGHT]:
        Configuracion.x += Configuracion.velocidad

    if Movimiento[pygame.K_UP]:
        Configuracion.y -= Configuracion.velocidad

    if Movimiento[pygame.K_DOWN]:
        Configuracion.y += Configuracion.velocidad

    #9. Limpiar la ventana
    ventana.fill(TRANSPARENTE)
    #10. Dibujar elementos en la ventana
    Configuracion.mostrar(ventana)
    #11. Actualizar la ventana
    pygame.display.filp()
    #12. Ralentizar un poco las cosas
    reloj.tick(FPS)