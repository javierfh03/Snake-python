from serpiente import Serpiente
from mapa import Mapa
from ventana import Ventana

s = Serpiente()
m = Mapa(s)
v = Ventana(m)

v.bucle()
