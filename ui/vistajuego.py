from time import sleep
from entities import *
from . import *
import sys


class VistaJuego:
    def __init__(self, ventana: Surface):
        self.ventana = ventana
        self.activa = True
        self.__fuente_texto = pygame.font.SysFont("Arial", 30)
        self.serpiente = Serpiente()
        self.mapa = Mapa(self.serpiente)

        self.mapa.colocar_manzana()
        self.mapa.iniciar_serpiente()

    def iniciar(self):
        texto_fin = "Fin del juego"

        while self.activa:
            self.__entrada_teclado()
            self.mapa.mover_serpiente()

            if self.mapa.no_derrota:
                self.__dibujar()
            else:
                dibujar_texto(texto_fin, self.__fuente_texto, BLANCO, self.ventana,
                              obtener_centro_texto(self.__fuente_texto, texto_fin), 200)

            sleep(0.15)
            pygame.display.update()

        self.ventana.fill(NEGRO)

    def __dibujar(self):
        self.ventana.fill(NEGRO)
        self.__dibujar_puntos()
        self.__dibujar_tablero()

        pygame.display.flip()

    def __dibujar_puntos(self):
        texto_puntos = "Puntos: {}".format(self.serpiente.puntos)

        dibujar_texto(texto_puntos, self.__fuente_texto, BLANCO, self.ventana,
                      obtener_centro_texto(self.__fuente_texto, texto_puntos), 10)

    def __dibujar_tablero(self):
        x = 0
        y = 50

        for i in range(0, len(self.mapa.vector)):
            for a in range(0, len(self.mapa.vector[i])):
                if self.mapa.vector[i][a] == 1:
                    pygame.draw.rect(self.ventana, VERDE, (x, y, 30, 30))
                elif self.mapa.vector[i][a] == 2:
                    pygame.draw.circle(self.ventana, ROJO, ((x + 15), (y + 15)), 15)
                x = x + 30
            x = 0
            y = y + 30

    def __entrada_teclado(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_w]:
                    self.serpiente.cambiar_direccion('w')
                elif keys[pygame.K_s]:
                    self.serpiente.cambiar_direccion('s')
                elif keys[pygame.K_a]:
                    self.serpiente.cambiar_direccion('a')
                elif keys[pygame.K_d]:
                    self.serpiente.cambiar_direccion('d')
                elif keys[pygame.K_ESCAPE]:
                    self.activa = False
