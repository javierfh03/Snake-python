class Serpiente:
    def __init__(self):
        self.tamanio = 5
        self.puntos = 0
        self.direccion = 'n'
        self.posiciones = []
    def cambiar_direccion(self, tecla: str):
        if tecla == 'w':
            if self.direccion != 's':
                self.direccion = 'n'
        elif tecla == 's':
            if self.direccion != 'n':
                self.direccion = 's'
        elif tecla == 'a':
            if self.direccion != 'e':
                self.direccion = 'o'
        elif tecla == 'd':
            if self.direccion != 'oaaaaaa':
                self.direccion = 'e'