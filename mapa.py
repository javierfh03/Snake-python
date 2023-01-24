import numpy as np
import random as ran
from serpiente import Serpiente

class Mapa:
    def __init__(self, serpiente: Serpiente):
        self.vector = np.zeros((15, 15))
        self.serpiente = serpiente
        self.no_derrota = True
        self.__anterior_pos = ()

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
        x = self.serpiente.posiciones[0][1]

        if self.serpiente.direccion == 'n':
            y -= 1
        elif self.serpiente.direccion == 's':
            y += 1
        elif self.serpiente.direccion == 'e':
            x += 1
        elif self.serpiente.direccion == 'o':
            x -= 1

        self.__detectar_colisiones(y, x)

    def __mover_posiciones(self):
        self.__anterior_pos = self.serpiente.posiciones[-1]
        self.vector[self.__anterior_pos[0]][self.__anterior_pos[1]] = 0

        # La posición de atrás recoge la de adelante y así continuamente
        for i in range(len(self.serpiente.posiciones) - 1, 0, -1):
            self.serpiente.posiciones[i] = self.serpiente.posiciones[i - 1]

    def __detectar_colisiones(self, y : int, x : int):
        # Comprobar que la serpiente no tocó ningún límite
        if 15 > y > -1 and 15 > x > -1:
            # Si el vector ya es uno, significa que ya estaba ahí la serpiente
            if self.vector[y][x] == 1:
                self.no_derrota = False
            else:
                self.__comer_manzana(y, x)
                self.serpiente.posiciones[0] = (y, x)
                self.vector[y][x] = 1
        else:
            self.no_derrota = False

    def __comer_manzana(self, y : int, x : int):
        if self.vector[y][x] == 2:
            self.serpiente.puntos += 1
            self.serpiente.posiciones.append(self.__anterior_pos)
            self.colocar_manzana()




