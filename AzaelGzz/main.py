#1. Importar el framework o paquete
import pygame
import sys
#2. Definir constantes
ANCHO_VENTANA = 640
ALTO_VENTANA = 480
NEGRO = (0, 0, 0)
FPS = 30
#3. Inicializar pygame
pygame.init()
#4. Cargar recursos (imagenes)
imagen_perfil = pygame.image.load("AzaelGzz/imagendvd.png")
#5. Inicializar variables
ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Mover Foto de Perfil")
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
#6. Ciclo infinito
ventana.fill(NEGRO)
while True:
    #7. Verificar y manejar los eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #8. Realizar cualquier acción por frame
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        perfil.x -= perfil.velocidad
    if teclas[pygame.K_RIGHT]:
        perfil.x += perfil.velocidad
    if teclas[pygame.K_UP]:
        perfil.y -= perfil.velocidad
    if teclas[pygame.K_DOWN]:
        perfil.y += perfil.velocidad

    #9. Limpiar la ventana
    ventana.fill(NEGRO) 
    #10. Dibujar elementos en la ventana
    perfil.mostrar(ventana)
    #11. Actualizar la ventana
    pygame.display.flip()
    #12. Ralentizar un poco las cosas
    reloj.tick(FPS)