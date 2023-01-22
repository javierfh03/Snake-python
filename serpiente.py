class Serpiente:
    def __init__(self):
        self.tamanio = 5
        self.puntos = 0
        self.direccion = 'n'
        self.posiciones = []
    def cambiar_direccion(self, tecla: str):
        if tecla == 'w':
            self.direccion = 'n'
        elif tecla == 's':
            self.direccion = 's'
        elif tecla == 'a':
            self.direccion = 'o'
        elif tecla == 'd':
            self.direccion = 'e'