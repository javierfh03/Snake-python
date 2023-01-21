from serpiente import Serpiente
from mapa import Mapa

s = Serpiente()
m = Mapa(s)

m.iniciar_serpiente()

for i in range(0, 15):
    for a in range(0, 15):
        print(m.vector[i][a], end=" ")

    print()

print("----------------------------------------------------------")
s.cambiar_direccion('d')
m.mover_serpiente()

for i in range(0, 15):
    for a in range(0, 15):
        print(m.vector[i][a], end=" ")

    print()

