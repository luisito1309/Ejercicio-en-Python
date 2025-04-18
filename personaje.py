import pygame
import constante

class Personaje():
    def __init__(self, x, y):
        self.forma = pygame.Rect(0, 0, constante.alto_personaje, constante.ancho_personaje)
        self.forma.center = (x, y)
        
    def dibujar(self, interfaz):
        pygame.draw.rect(interfaz, constante.color_personaje, self.forma)
