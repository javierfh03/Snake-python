from ui.utilidades import dibujar_texto
from ui.utilidades import obtener_centro_texto
from ui.utilidades import VERDE

import sys

import pygame
from pygame.surface import Surface


class VistaMenu:
    def __init__(self, ventana: Surface):
        self.ventana = ventana
        self.activa = True
        self.__fuente_titulo = pygame.font.SysFont("Arial", 90)
        self.__fuente_texto = pygame.font.SysFont("Arial", 30)

    def ejecutar(self):
        self.__dibujar()
        self.__entrada_mouse()

        pygame.display.update()

    def __dibujar(self):
        texto_titulo = "Snake"
        texto_jugar = "Jugar"
        texto_salir = "Salir"

        self.titulo = dibujar_texto(texto_titulo, self.__fuente_titulo, VERDE, self.ventana,
                                    obtener_centro_texto(self.__fuente_titulo, texto_titulo,
                                                         self.ventana.get_width()), 40)
        self.jugar = dibujar_texto(texto_jugar, self.__fuente_texto, VERDE, self.ventana,
                                   obtener_centro_texto(self.__fuente_texto, texto_jugar,
                                                        self.ventana.get_width()), 230)
        self.salir = dibujar_texto(texto_salir, self.__fuente_texto, VERDE, self.ventana,
                                   obtener_centro_texto(self.__fuente_texto, texto_salir,
                                                        self.ventana.get_width()), 330)

        pygame.display.flip()

    def __entrada_mouse(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                if self.jugar.get_rect(center=(220, 240)).collidepoint(pos):
                    self.activa = False
                if self.salir.get_rect(center=(220, 340)).collidepoint(pos):
                    pygame.quit()
                    sys.exit()
