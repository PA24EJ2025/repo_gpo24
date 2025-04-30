import pygame
import sys

pygame.init()

ventana = pygame.display.set_mode((600, 400))
reloj = pygame.time.Clock()

class Perfil:
    def __init__(self, x, y, alto, ancho, velocidad):
        self.x = x
        self.y = y
        self.alto = alto
        self.ancho = ancho
        self.velocidad = velocidad
        self.imagen = pygame.image.load("jesusgarzamtz/dbchihl-d82fbe86-c8a6-4ca9-a719-7eddd7583d11.png")

perfil = Perfil(100, 100, 80, 80, 5)

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                perfil.x -= perfil.velocidad
            if evento.key == pygame.K_RIGHT:
                perfil.x += perfil.velocidad
            if evento.key == pygame.K_UP:
                perfil.y -= perfil.velocidad
            if evento.key == pygame.K_DOWN:
                perfil.y += perfil.velocidad

    ventana.fill((255, 255, 255))
    ventana.blit(perfil.imagen, (perfil.x, perfil.y))
    pygame.display.update()
    reloj.tick(30)
