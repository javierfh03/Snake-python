from entities.serpiente import Serpiente
from entities.mapa import Mapa
from ui.ventanajuego import VentanaJuego

s = Serpiente()
m = Mapa(s)
v = VentanaJuego(m)

v.iniciar()


