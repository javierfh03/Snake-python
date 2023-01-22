import numpy as np
import random as ran
from serpiente import Serpiente

class Mapa:
    def __init__(self, serpiente: Serpiente):
        self.vector = np.zeros((15, 15))
        self.serpiente = serpiente

    def colocar_manzana(self):
        while True:
            y = ran.randint(0, 14)
            x = ran.randint(0, 14)

            dato = self.vector[y][x]

            if dato == 0:
                self.vector[y][x] = 2
                break

    def iniciar_serpiente(self):
        for i in range(4, 9):
            self.vector[i][7] = 1
            self.serpiente.posiciones.append([i, 7])

    def mover_serpiente(self):
        self.__mover_posiciones()
        y = self.serpiente.posiciones[0][0]
        x = self.serpiente.posiciones[1][1]

        if self.serpiente.direccion == 'n':
            y -= 1
        elif self.serpiente.direccion == 's':
            y += 1
        elif self.serpiente.direccion == 'e':
            x += 1
        elif self.serpiente.direccion == 'o':
            x -= 1

        self.serpiente.posiciones[0] = (y, x)
        self.vector[y][x] = 1

    def __mover_posiciones(self):
        ultimo = self.serpiente.posiciones[-1]

        self.vector[ultimo[0]][ultimo[1]] = 0

        for i in range(len(self.serpiente.posiciones) - 1, 0, -1):
            self.serpiente.posiciones[i] = self.serpiente.posiciones[i - 1]






