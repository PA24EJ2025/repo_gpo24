class Perfil:
    def __init__(self, x, y, ancho, alto, imagen, velocidad):
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = alto
        self.imagen = imagen
        self.velocidad = velocidad
        self.fotoperfil = pygame.image.load("ousi.png")
    def mostrar(self, ventana):
        ventana.blit(self.fotoperfil, (self.x, self.y))

import pygame
import sys
pygame.init()
ventana = pygame.display.set_mode((800, 700))
reloj = pygame.time.Clock()
frames = 60

posicion = Perfil(x=350, y=300, alto=80, ancho=80, velocidad=5) 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        posicion.y -= posicion.velocidad  
    if keys[pygame.K_DOWN]:
        posicion.y += posicion.velocidad
    if keys[pygame.K_LEFT]:
        posicion.x -= posicion.velocidad 
    if keys[pygame.K_RIGHT]:
        posicion.x += posicion.velocidad 

    ventana.fill("black") #optimizacion para asignar color al fondo sin necesidad de una constante 
    posicion.mostrar(ventana)
    pygame.display.flip()
    reloj.tick(frames)