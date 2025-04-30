#1. Importar el framework o paquete
import pygame
import sys 
from pygame.locals import *

#2. Definir constantes
ANCHO_VENTANA=640
ALTO_VENTANA=480
FPS = 60
BLANCO=(255,255,255)
#3. Inicializar pygame
pygame.init()
ventana = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.display.set_caption("MOVER FOTO DE PERFIL")
reloj=pygame.time.Clock()

#4. Cargar recursos (imagenes)
imagen_perfil = pygame.image.load("berenice07191/foto_perfil.png")
imagen_perfil= pygame.transform.scale(imagen_perfil,(80,80))

class Perfil:
    def _init_(self,x,y,alto,ancho,velocidad):
        self.x= x
        self.y=y
        self.alto=alto
        self.ancho=ancho
        self.velocidad=velocidad
        self.imagen=imagen_perfil

    def mostrar(self,ventana):
        ventana.blit(self.imagen,(self.x,self.y))
    def mover(self,teclas):
        if teclas[K_LEFT]:
            self.x-=self.velocidad
        if teclas[K_RIGHT]:
            self.x+= self.velocidad
        if teclas[K_UP]:
            self.y-=self.velocidad
        if teclas[K_DOWN]:
            self.y+=self.velocidad

        self.x=max(0,min(self.x,ANCHO_VENTANA-self.ancho))
        self.y=max(0,min(self.y,ALTO_VENTANA-self.alto))


#5. Inicializar variables
Perfil=Perfil(100,100,80,80,5)
#6. Ciclo infinito
while True:
    #7. Verificar y manejar los eventos
    for evento in pygame.event.get():
        if evento.type==QUIT:
            pygame.quit()
            sys.exit()
    #8. Realizar cualquier acción por frame
    teclas= pygame.key.get_pressed()
    Perfil.mover(teclas)
    #9. Limpiar la ventana
    ventana.fill((255,255,255))
    #10. Dibujar elementos en la ventana
    Perfil.mostrar(ventana)
    #11. Actualizar la ventana
    pygame.display.update()
    #12. Ralentizar un poco las cosas
    reloj.tick(FPS)