import pygame
import constante
from personaje import Personaje

pygame.init()

jugador = Personaje(x=50, y=50)

ventana = pygame.display.set_mode((constante.ancho_Ventana, constante.alto_Ventana))
pygame.display.set_caption("JUAN JESUS ROBLES")

#definir las variable de movimientos

mover_arriba = False
mover_abajo = False
mover_izquierda = False
mover_derecha = False



run = True
while run:

    #calcular el movimiento del jugador

    delta_x = 0
    delta_y = 0

    if mover_derecha == True:
        delta_x = 5
    if mover_izquierda == True:
        delta_x = -5
    if mover_arriba == True:
        delta_y = -5
    if mover_abajo == True:
        delta_y = 5
    
    #mover al jugador

    jugador.movimiento (delta_x, delta_y)

    ventana.fill((0, 0, 0))
    jugador.dibujar(ventana)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.k_a:
            mover_izquierda = True
        if event.key == pygame.k_d:
            mover_derecha = True
        if event.key == pygame.k_w:
            mover_arriba = True
        if event.key == pygame.k_s:
            mover_abajo = True

    pygame.display.update()

pygame.quit()
