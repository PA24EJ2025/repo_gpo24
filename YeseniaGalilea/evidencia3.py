import pygame
import sys 

pygame.init()
 
ANCHO, ALTO = 500, 500
VENTANA = pygame.display.set_mode((ANCHO, ALTO))

COLOR_FONDO = (0, 0, 0)
FPS = 60
clock = pygame.time.Clock() 

class Perfil:
    def __init__(self, x, y, alto, ancho, ruta_imagen, velocidad):
        self.imagen = pygame.image.load(ruta_imagen)
        self.imagen = pygame.transform.scale(self.imagen, (ancho, alto))
        self.rect = self.imagen.get_rect()
        self.rect.topleft = (x, y)
        self.velocidad = velocidad
       
    def mover(self, teclas):
        if teclas[pygame.K_LEFT]:
            self.rect.x -= self.velocidad
        if teclas[pygame.K_RIGHT]:
            self.rect.x += self.velocidad 
        if teclas[pygame.K_UP]:
            self.rect.y -= self.velocidad
        if teclas[pygame.K_DOWN]:
            self.rect.y += self.velocidad 
                
    def dibujar(self, ventana):
        ventana.blit(self.imagen, self.rect)

imagen = Perfil(100, 100, 80, 80, 'YeseniaGalilea/foto.jpg', 5)

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
              
    teclas = pygame.key.get_pressed()
    imagen.mover(teclas)
            
    VENTANA.fill(COLOR_FONDO)
    imagen.dibujar(VENTANA)
            
    pygame.display.update()
    clock.tick(FPS)
              

      
        