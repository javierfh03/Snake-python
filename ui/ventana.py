from ui.__init__ import *
from ui.vistajuego import VistaJuego
from ui.vistamenu import VistaMenu


class Ventana:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Snake")

    def iniciar(self):
        venpygame = pygame.display.set_mode((ANCHURA, ALTURA))
        menu = VistaMenu(venpygame)

        while True:
            if menu.activa:
                menu.ejecutar()
            else:
                juego = VistaJuego(venpygame)
                juego.iniciar()

                menu.activa = True

