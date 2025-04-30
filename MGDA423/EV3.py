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

#5. Inicializar variables
x = 80
y = 80
velocidad = 5

#6. ciclo infinito..
while True:
     #7. Verificar y manejar los eventos

     for evento in pygame.event.get():
         if evento.type == QUIT:
             pygame.quit()

             sys.exit()
         if evento.type == KEYDOWN:
             if evento.key == K_UP:
                 y -= velocidad
             if evento.key == K_DOWN:
                 y += velocidad
             if evento.key == K_LEFT:
                 x -= velocidad
             if evento.key == K_RIGHT:
                 x += velocidad                

     #8. Realizar cualquier acción por frame

     #9. Limpiar la ventana
     ventana.fill(AZUL_CLARO)

     #10. Dibujar elementos en la ventana
     ventana.blit(foto,(x,y))

     #11... Actualizar la ventana
     pygame.display.update()

     #12. Ralentizar un poco las cosas
     reloj.tick(CUADROS_POR_SEGUNDO)

 