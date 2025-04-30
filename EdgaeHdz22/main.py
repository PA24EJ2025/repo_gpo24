import pygame
import sys

ANCHO_VENTANA = 600
ALTO_VENTANA = 400
COLOR_FONDO = (30, 30, 30)
NEGRO = (0, 0, 0)
FPS = 60

pygame.init()

imagen_perfil = pygame.image.load("EdgaeHdz22/perfil.png")

ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Mover foto de perfil")
reloj = pygame.time.Clock()

class Perfil:
    def __init__(self, x, y, alto, ancho, velocidad):
        self.x = x
        self.y = y
        self.alto = alto
        self.ancho = ancho
        self.velocidad = velocidad
        self.imagen = pygame.transform.scale(imagen_perfil, (self.ancho, self.alto))

    def mostrar(self, ventana):
        ventana.blit(self.imagen, (self.x, self.y))

perfil = Perfil(x=100, y=100, alto=80, ancho=80, velocidad=5)

ventana.fill(NEGRO) 
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        perfil.x -= perfil.velocidad
    if teclas[pygame.K_RIGHT]:
        perfil.x += perfil.velocidad
    if teclas[pygame.K_UP]:
        perfil.y -= perfil.velocidad
    if teclas[pygame.K_DOWN]:
        perfil.y += perfil.velocidad

    ventana.fill(NEGRO)
    perfil.mostrar(ventana)
    pygame.display.flip()
    reloj.tick(FPS)
