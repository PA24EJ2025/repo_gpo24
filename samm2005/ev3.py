import pygame
import sys
pygame.init()


ANCHO, ALTO = 1000, 1000
VENTANA = pygame.display.set_mode((ANCHO, ALTO))

MORADO = (182, 149, 192)


class FotoPerfil:
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


imagen = FotoPerfil(100, 100, 80, 80, 'samm2005/abeja.png', 5)


while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    teclas = pygame.key.get_pressed()
    imagen.mover(teclas)  

    VENTANA.fill(MORADO)  
    imagen.dibujar(VENTANA)  

    pygame.display.update()  
