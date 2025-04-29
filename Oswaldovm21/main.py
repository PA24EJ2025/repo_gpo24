#1. Importar el framework o paquete
import pygame
from pygame.locals import *
import sys
import modulo
#2. Definir constantes
ANCHO_VENTANA = 640
ALTO_VENTANA = 480
FPS = 30
NEGRO = (0,0,0,)

#3. Inicializar pygame
pygame.init()
ventana = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
reloj = pygame.time.Clock()
#4. Cargar recursos (imagenes)
alto = 80
ancho = 80
imagen = pygame.image.load("Oswaldovm21/Cyndaquil.png").convert_alpha()
imagen = pygame.transform.scale(imagen, (alto, ancho))
imgrect = imagen.get_rect()
#5. Inicializar variables
x = (ANCHO_VENTANA - 80)//2
y = (ALTO_VENTANA - 80)//2
velocidad = 5
#6. Ciclo infinito
ventana.fill(NEGRO)
while True:
    #7. Verificar y manejar los eventos
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
    #8. Realizar cualquier acción por frame
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        x -= velocidad
        
    #9. Limpiar la ventana
    ventana.fill(NEGRO)
    #10. Dibujar elementos en la ventana
    ventana.blit(imagen, (x, y))
    pygame.display.flip()
    #11. Actualizar la ventana
    
    #12. Ralentizar un poco las cosas
    pygame.time.Clock().tick(30)