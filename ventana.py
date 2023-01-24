import sys
from time import sleep

import pygame
from mapa import Mapa

class Ventana:
    def __init__(self, mapa: Mapa):
        pygame.init()
        pygame.display.set_caption("Snake")
        self.ventana = pygame.display.set_mode((450, 500))
        self.mapa = mapa

        mapa.colocar_manzana()
        mapa.iniciar_serpiente()

        self.__dibujar()

    def __dibujar(self):
        x = 0
        y = 50
        verde = (0, 255, 0)
        rojo = (255, 0, 0)

        self.ventana.fill((0, 0, 0))

        for i in range(0, len(self.mapa.vector)):
            for a in range(0, len(self.mapa.vector[i])):
                if self.mapa.vector[i][a] == 1:
                    pygame.draw.rect(self.ventana, verde, (x, y, 30, 30))
                elif self.mapa.vector[i][a] == 2:
                    pygame.draw.rect(self.ventana, rojo, (x, y, 30, 30))
                    # pygame.draw.circle(self.ventana, rojo, (x, y), 15)
                x = x + 30
            x = 0
            y = y + 30
        pygame.display.flip()

    def bucle(self):
        while True:
            self.__entrada_teclado()
            self.mapa.mover_serpiente()
            self.__dibujar()
            sleep(0.1)

            pygame.display.update()

    def __entrada_teclado(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_w]:
                    self.mapa.serpiente.cambiar_direccion('w')
                elif keys[pygame.K_s]:
                    self.mapa.serpiente.cambiar_direccion('s')
                elif keys[pygame.K_a]:
                    self.mapa.serpiente.cambiar_direccion('a')
                elif keys[pygame.K_d]:
                    self.mapa.serpiente.cambiar_direccion('d')
                elif keys[pygame.K_ESCAPE]:
                    pygame.quit()
                    sys.exit()