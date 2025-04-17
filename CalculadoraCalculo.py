import pygame
import constante
from Botones import Botones

pygame.init()

ventana = pygame.display.set_mode((constante.ancho_Ventana, constante.alto_Ventana))
pygame.display.set_caption("Calculadora de Calculo")

jugador = Botones(x=50, y=50)

run = True
while run:
    ventana.fill((0, 0, 0))
    jugador.dibujar(ventana)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
