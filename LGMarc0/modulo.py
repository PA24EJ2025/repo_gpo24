import pygame 

pygame.init()

WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Movimiento Perfil")

class Perfil:
    def __init__(self, x, y, velocidad):
        self.ancho = 80
        self.alto = 80
        self.x = x
        self.y = y
        self.velocidad = velocidad
        self.imagen = pygame.image.load("C:\\Users\\marco\\repo_gpo24\\LGMarc0\\perfil.png")
        self.imagen = pygame.transform.scale(self.imagen, (self.ancho, self.alto))

    def mover(self, teclas):
        if teclas[pygame.K_a] and self.x > 0:
            self.x -= self.velocidad
        if teclas[pygame.K_d] and self.x + self.ancho < WIDTH:
            self.x += self.velocidad
        if teclas[pygame.K_w] and self.y > 0:
            self.y -= self.velocidad
        if teclas[pygame.K_s] and self.y + self.alto < HEIGHT:
            self.y += self.velocidad

    def dibujar(self, superficie):
        superficie.blit(self.imagen, (self.x, self.y))

perfil = Perfil(x=WIDTH // 2, y=HEIGHT // 2, velocidad=5)
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    teclas = pygame.key.get_pressed()
    perfil.mover(teclas)

    SCREEN.fill((255, 255, 255))
    perfil.dibujar(SCREEN)
    pygame.display.update()
    clock.tick(60)

pygame.quit()