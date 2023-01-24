import sys
from time import sleep

import pygame
from mapa import Mapa

class Ventana:
    __anchura = 450
    __altura = 500
    __verde = (0, 255, 0)
    __rojo = (255, 0, 0)
    __negro = (0, 0, 0)
    __blanco = (255, 255, 255)

    def __init__(self, mapa: Mapa):
        pygame.init()
        pygame.display.set_caption("Snake")
        self.ventana = pygame.display.set_mode((self.__anchura, self.__altura))
        self.mapa = mapa
        self.__fuente_texto = pygame.font.SysFont("Arial", 30)

        mapa.colocar_manzana()
        mapa.iniciar_serpiente()

    def bucle(self):
        while self.mapa.no_derrota:
            self.__entrada_teclado()
            self.mapa.mover_serpiente()
            self.__dibujar()
            sleep(0.1)

            pygame.display.update()

        self.__dibujar_fin()
        sleep(2)



    def __dibujar(self):

        self.ventana.fill(self.__negro)
        self.__dibujar_puntos()
        self.__dibujar_tablero()

        pygame.display.flip()

    def __dibujar_puntos(self):
        texto = "Puntos: {}".format(self.mapa.serpiente.puntos)
        texto_tamanio = self.__fuente_texto.render(texto, True, self.__blanco).get_size()
        x = (self.__anchura - texto_tamanio[0]) / 2

        self.ventana.blit(self.__fuente_texto.render(texto, True, self.__blanco), (x, 10))

    def __dibujar_tablero(self):
        x = 0
        y = 50

        for i in range(0, len(self.mapa.vector)):
            for a in range(0, len(self.mapa.vector[i])):
                if self.mapa.vector[i][a] == 1:
                    pygame.draw.rect(self.ventana, self.__verde, (x, y, 30, 30))
                elif self.mapa.vector[i][a] == 2:
                    pygame.draw.circle(self.ventana, self.__rojo, ((x + 15), (y + 15)), 15)
                x = x + 30
            x = 0
            y = y + 30

    def __dibujar_fin(self):
        texto = "Fin del juego"
        texto_tamanio = self.__fuente_texto.render(texto, True, self.__blanco).get_size()
        x = (self.__anchura - texto_tamanio[0]) / 2
        y = (self.__anchura - texto_tamanio[1]) / 2

        self.ventana.blit(self.__fuente_texto.render(texto, True, self.__blanco), (x, y))
        pygame.display.flip()

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