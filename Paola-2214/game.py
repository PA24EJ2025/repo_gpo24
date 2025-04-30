import pygame 
import sys
from pygame.locals import*

x= 0
y=0
alto= 650
ancho = 600
velocidad= 30
pygame.init()
ventana= pygame.display.set_mode((ancho,alto))
reloj = pygame.time.Clock()

class Perfil:
    def __init__(self,x,y,alto,ancho,velocidad):
        self.x = x
        self.y = y
        self.alto = alto
        self.ancho = ancho
        self.velocidad = velocidad
        self.imagen = pygame.image.load('Paola-2214/snoopy_perfil.jpg')  
        self.imagen_nueva = pygame.transform.scale(self.imagen,(80,80))

    def mostrar(self,ventana):
        ventana.blit(self.imagen_nueva,(self.x, self.y))

foto = Perfil(x,y,alto,ancho,velocidad)

while True:
    for evento in pygame.event.get():
        if evento.type ==QUIT:
            pygame.quit()
            sys.exit()

    
        elif evento.type ==pygame.KEYDOWN:   
            if evento.key == K_UP:
                foto.y -= foto.velocidad
            if evento.key == K_DOWN:
                foto.y += foto.velocidad
            if evento.key == K_LEFT:
                foto.x -= foto.velocidad
            if evento.key == K_RIGHT:
                foto.x += foto.velocidad

    ventana.fill((0,0,0))
    foto.mostrar(ventana)
    pygame.display.flip()
    reloj.tick(velocidad)

    

