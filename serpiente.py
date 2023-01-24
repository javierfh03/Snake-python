class Serpiente:
    def __init__(self):
        self.tamanio = 5
        self.puntos = 0
        self.direccion = 'n'
        self.posiciones = []

    def cambiar_direccion(self, tecla: str):
        # En caso de que se intente cambiar la dirección a la contraria a la que se está dirigiendo no se permitirá
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
            if self.direccion != 'o':
                self.direccion = 'e'
