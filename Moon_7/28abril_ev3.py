#EVIDENCIA 3 PROGRAMACION AVANZADA

import pygame
from pygame.locals import *
import perfil
import sys

<<<<<<< HEAD

ALTO_VENTANA=500
ANCHO_VENTANA=700
MORADO = (182, 149, 192)
FPS=40
SIZE_CUADRO=70
ANCHO_MAX=ANCHO_VENTANA-SIZE_CUADRO
ALTO_MAX=ALTO_VENTANA-SIZE_CUADRO

=======
ALTO_VENTANA=500
ANCHO_VENTANA=700
MORADO = (182, 149, 192)
FPS=40
SIZE_CUADRO=70
ANCHO_MAX=ANCHO_VENTANA-SIZE_CUADRO
ALTO_MAX=ALTO_VENTANA-SIZE_CUADRO

>>>>>>> fc2090003b82904aa7f455d420d2ebed377a3a06
pygame.init()
ventana = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
reloj = pygame.time.Clock()

class perfil:
  def __init__(self,x,y,alto,ancho,ruta_imagen):
     self.x=x
     self.y=y
     self.alto=alto
     self.anncho=ancho
     self.imagen = pygame.image.load(ruta_imagen)
     
def mover(self,ventana):
  ventana.blit(self.imagen,
               (self.x,self.y,
               self.ancho,self.alto))
    
def dibujar(self,ventana):
    ventana.blit(self.imagen,
                 (self.x,self.y,
                  self.ancho,self.alto))
    
imagen=perfil(90,90,60,60, 'Moon_7/perfil.png')

while True:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
            

    
    pygame.display.update()
    reloj.tick(FPS) 
<<<<<<< HEAD
    
=======
    
>>>>>>> fc2090003b82904aa7f455d420d2ebed377a3a06
