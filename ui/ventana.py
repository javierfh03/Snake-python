from ui.__init__ import *
from ui.vistajuego import VistaJuego


class Ventana:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Snake")
        self.venpygame = pygame.display.set_mode((ANCHURA, ALTURA))
        VistaJuego(self.venpygame).iniciar()

