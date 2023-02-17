from ui.vistajuego import VistaJuego
from ui.vistamenu import VistaMenu

import pygame


class Ventana:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Snake")
        self.anchura = 450
        self.altura = 500

    def iniciar(self):
        venpygame = pygame.display.set_mode((self.anchura, self.altura))
        menu = VistaMenu(venpygame)

        while True:
            if menu.activa:
                menu.ejecutar()
            else:
                juego = VistaJuego(venpygame)
                juego.iniciar()

                menu.activa = True

