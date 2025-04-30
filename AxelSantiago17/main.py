#1. Importar el framework o paquete
import pygame
from pygame.locals import*
import sys
from modulo import Perfil

#2. Definir constantes
ANCHO = 80
ALTO = 80
FPS = 30 
BLANCO = (255,255,255)

#3. Inicializar pygame
pygame.init()
ventana = pygame.display.set_mode((ANCHO, ALTO))
reloj = pygame.time.Clock()

#4. Cargar recursos (imagenes)
personaje = Perfil(ANCHO//2, ALTO//2, 80, 80, 8)
#5. Inicializar variables

#6. Ciclo infinito
while True:
    #7. Verificar y manejar los eventos
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
    #8. Realizar cualquier acción por frame
    keys = pygame.key.get_pressed()
    if keys[K_LEFT]: personaje.x -= personaje.velocidad
    if keys[K_RIGHT]: personaje.x += personaje.velocidad
    if keys[K_UP]: personaje.y -= personaje.velocidad
    if keys[K_DOWN]: personaje.y += personaje.velocidad

    personaje.pos_x = max(0, min(personaje.pos_x, ANCHO - personaje.ancho))
    personaje.pos_y = max(0, min(personaje.pos_y, ALTO - personaje.alto))

    #9. Limpiar la ventana
    ventana.fill(BLANCO)

    #10. Dibujar elementos en la ventana}
    ventana.blit(personaje.imagen, (personaje.x, personaje.y))
    
    #11. Actualizar la ventana
    pygame.display.update()
    
    #12. Ralentizar un poco las cosas
    reloj.tick(FPS)
